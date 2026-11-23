"""Issue #18 tests.

Unit-level: checks the catalog view logic directly.
Route-level: checks catalog response time through HTTP requests.
"""


import math
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pytest
from werkzeug.serving import make_server

from app import app


USERS_PER_WAVE = 100
WAVES = 20
TIME_LIMIT_SECONDS = 2.0


@pytest.fixture
def catalog_url():
    server = make_server("127.0.0.1", 0, app, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    yield f"http://127.0.0.1:{server.server_port}/"

    server.shutdown()
    thread.join()
    server.server_close()


def request_catalog(url, barrier):
    barrier.wait(timeout=15)
    started = time.perf_counter()

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            response.read()
            elapsed = time.perf_counter() - started
            return response.status, elapsed, None
    except Exception as error:
        elapsed = time.perf_counter() - started
        return None, elapsed, str(error)


def test_catalog_response_time_under_100_simultaneous_users(catalog_url):
    results = []

    with ThreadPoolExecutor(max_workers=USERS_PER_WAVE) as pool:
        for _ in range(WAVES):
            barrier = threading.Barrier(USERS_PER_WAVE)
            wave = list(
                pool.map(
                    lambda _: request_catalog(catalog_url, barrier),
                    range(USERS_PER_WAVE),
                )
            )
            results.extend(wave)

    failed_requests = [
        error for status, _, error in results if status != 200
    ]
    assert not failed_requests, (
        f"{len(failed_requests)} requests failed; first error: "
        f"{failed_requests[0]}"
    )

    latencies = sorted(elapsed for _, elapsed, _ in results)
    required_successes = math.ceil(0.95 * len(results))
    within_limit = sum(
        elapsed <= TIME_LIMIT_SECONDS
        for _, elapsed, _ in results
    )
    p95 = latencies[math.ceil(0.95 * len(latencies)) - 1]

    assert within_limit >= required_successes, (
        f"{within_limit}/{len(results)} requests completed within "
        f"{TIME_LIMIT_SECONDS}s; required {required_successes}"
    )
    assert p95 <= TIME_LIMIT_SECONDS, (
        f"95th percentile was {p95:.3f}s; limit is {TIME_LIMIT_SECONDS}s"
    )
