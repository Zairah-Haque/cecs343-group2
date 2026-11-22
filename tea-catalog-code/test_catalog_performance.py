import math
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor


CATALOG_URL = "http://127.0.0.1:5000/"
USERS_PER_WAVE = 100
WAVES = 20
TIME_LIMIT_SECONDS = 2.0


def request_catalog(barrier):
    try:
        barrier.wait(timeout=15)
        started = time.perf_counter()

        with urllib.request.urlopen(CATALOG_URL, timeout=10) as response:
            response.read()
            elapsed = time.perf_counter() - started
            return response.status, elapsed

    except Exception:
        elapsed = time.perf_counter() - started if "started" in locals() else 0
        return None, elapsed


def test_catalog_response_time_under_100_simultaneous_users():
    results = []

    with ThreadPoolExecutor(max_workers=USERS_PER_WAVE) as pool:
        for _ in range(WAVES):
            barrier = threading.Barrier(USERS_PER_WAVE)
            wave = list(
                pool.map(
                    request_catalog,
                    [barrier] * USERS_PER_WAVE,
                )
            )
            results.extend(wave)

    latencies = sorted(elapsed for _, elapsed in results)
    successful_requests = sum(
        status == 200 and elapsed <= TIME_LIMIT_SECONDS
        for status, elapsed in results
    )
    required_successes = math.ceil(0.95 * len(results))
    p95 = latencies[math.ceil(0.95 * len(latencies)) - 1]

    assert successful_requests >= required_successes, (
        f"{successful_requests}/{len(results)} requests returned HTTP 200 "
        f"within {TIME_LIMIT_SECONDS}s; required {required_successes}"
    )
    assert p95 <= TIME_LIMIT_SECONDS, (
        f"95th percentile was {p95:.3f}s; limit is {TIME_LIMIT_SECONDS}s"
    )
