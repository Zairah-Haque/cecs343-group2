| Task | PR deliverable | Depends on |
|---|---|---|
| **#7 Shipping page** | Reference and close #7. Meet its checklist for opening the page from the cart icon, showing item, quantity and price, handling an empty cart, and handling HTTP 503. Include unit and route-level tests. | — |
| **#8 `/teas`** | Reference and close #8. Put the existing test functions out of `tests/conftest.py` and in a collected test module; cover every checklist line with unit and route-level tests. `conftest.py` is for fixtures, so its test functions are not collected as tests. | — |
| **#10 Adding Tea Choice to Cart** | Reference and close #10. Cover its checklist with unit and route-level tests; adjust the implementation where those tests show a gap. | — |
| **#13 Compile Tea Catalog and Typology ★** | Reference and close #13. Cover its checklist with unit and route-level tests; adjust the implementation where needed. | — |
| **#14 Removing Tea From Cart** | Reference and close #14. Cover its checklist with unit and route-level tests; adjust the implementation where needed. | #10 |
| **#18 Catalog response time ★** | Reference and close #18. Add tests for the stated two-second, 95% and 100-simultaneous-user measure, and fix any failure. | #13 |
| **#19 Duplicate orders** | Reference and close #19. Test the stated 100 repeated-submission cases at unit and route level, and fix any failure. The repository’s requirements still have `[N]` and `[S]` placeholders; use the values in Issue #19 if it specifies them. | #10 |
| **#20 Password protection** | Reference and close #20. Test that stored passwords and backups do not contain readable passwords, and fix any failure. The code already has password hashing and backup handling, but the ZIP shows no tests for them. | — |
| **Coverage reporting ★** | Add the CI coverage command and dependency so a CI run produces the number required for `README.md`. The current workflow runs `pytest` only. | All feature/test PRs |
| **Verification Log ★** | Audit AI-assisted PRs merged since M2 and add one complete entry per PR, with all seven required fields. Use the required lowercase path `docs/verification-log.md`; the ZIP has `docs/Verification-log.md`. | PR-history audit; all PRs that need entries |
| **README evidence ★** | Update `## Coverage` with the number and command from the latest CI run, and update `## Verification debt` with the weighted count and date. The current debt line is dated Nov. 6, and there is no Coverage line. | Coverage reporting; Verification Log |
| **M3 beta contents ★** | Add root `CHANGELOG.md` entries, one line per closed Issue with its number, in a PR. After it merges, cut `release/0.9` from `main` and tag it `v0.9-beta`. | All eight Issue PRs; README evidence; Verification Log |

| Task | PR deliverable | Depends on |
|---|---|---|
| **M3 feedback response** | Add `docs/m3-response.md`, one sentence per feedback item naming the change and PR number, or why it was not changed. Include the Class 22 estimate beside actual time and one sentence explaining the difference. | M3 feedback is returned |
| **Decision records** | For each design or architecture change since M2, add a separate Class 13 style decision record. Include it with the PR making the change, or use a documentation PR if the change is already merged. | Identify changes from PR history |
| **Contribution reports** | Each member adds their own `docs/contributions/<github-username>.md` in a separate PR, covering the four required headings and checking claims against the merge history and Verification Log. | Semester PR history; generated-work log |
| **M4 Issue work** | For every Issue on the M4 milestone, make a PR that meets its acceptance criteria with the required tests, references the Issue, and closes it. If an Issue is dropped, use a PR that closes it with the `wontfix` label, comment and decision-record reference. | M4 Issue list and acceptance criteria |
| **Final release readiness** | Update `README.md` opening order and `## Coverage`; add the `v1.0` section above `v0.9-beta` in `CHANGELOG.md`; confirm the README commands work in a fresh Codespace. After merge, tag `v1.0` and require green CI on that tagged commit. | All M3/M4 Issue PRs; M3 response; contribution reports; decision records |
