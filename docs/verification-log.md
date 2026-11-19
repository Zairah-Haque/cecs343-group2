## PR #72 2026-11-19 @Biltzeebub
Tool and mode: Claude, Cowork
Requested: Corrected wording for the #13 entry (heading, Tool and mode, Disposition), after checking whether the #13 test was ever committed.
Generated: A replacement #13 entry of about 9 lines, a commit message and a PR description.
Claimed: The heading and Disposition are accurate: #13 is an Issue number with no PR, and the catalog-sort test is not in the repo.
Verified: The diff changes only the #13 heading and adds the Tool and mode and Disposition lines (+3 -1). The names get_catalog, harvest_year and price_per_gram appear in no code or test file, only in this log.
Not verified: Whether the test was ever written or run outside the repo, for example locally or in a chat. [minor]
Disposition: Accepted as drafted.

## PR #71 2026-11-19 @Biltzeebub
Tool and mode: Claude, chat
Requested: Draft Verification Log entries for PRs #59 and #64 from the repo history and earlier chats, and restore the entries lost in the PR #70 merge (all of #13 and the end of #14).
Generated: Two new entries (about 16 lines), the restored text for #13 and #14 (about 9 lines), and corrected Verified, Not verified and Disposition lines for #70.
Claimed: Each new entry matches what its PR changed and how it was checked; the restored #13 and #14 text matches the original file at commit 9cd19d5.
Verified: Compared each new entry against its PR's Files changed tab: #59 is two renames with 0 lines changed, #64 is README +20/-2. Compared the restored #13 and #14 text with the original file in the History tab at commit 9cd19d5.
Not verified: Whether the Verified lines of #59 and #64 describe exactly what I did, beyond the Codespace run. [minor]
Disposition: Accepted after editing the Verified and Disposition lines to match what I did.

## PR #70 2026-11-19 @Biltzeebub
Tool and mode: Claude, chat (single prompt)
Requested: Reorder the 12 existing log entries newest first and return the full file text to paste.
Generated: The 12 entries in new order with blank lines normalized, no entry text added or removed.
Claimed: Only the order and the spacing between entries changed; entry wording is unchanged.
Verified: The Files changed view showed the lowercase file name and the entries in newest-first order.
Not verified: The paste dropped the end of #14 and all of #13, which I found after the merge and restored in PR #71. The other entries were not compared character by character when merged. [minor]
Disposition: Accepted, then corrected in PR #71.

## PR #64 2026-11-15 @Biltzeebub
Tool and mode: Claude, chat
Requested: README run and test commands, so a fresh Codespace can start the app and run the tests using only the README (M3 requirement).
Generated: A "Running" and a "Testing" section for README.md, about 20 lines: pip install -r requirements.txt, cd tea-catalog-code, flask --app app run, the local URL, and pytest.
Claimed: Running those commands from the repository root starts the app and runs the tests.
Verified: The committed text is identical to the draft (checked against the diff). The commands were run on a scratch copy of the repo (pytest: 1 passed; /, /teas and /cart returned HTTP 200), and I ran them in a fresh Codespace on the PR branch, where they passed.
Not verified: A fresh Codespace on main after the merge, and later on release/0.9. [minor]
Disposition: Accepted as drafted, no edits.

## PR #59 2026-11-15 @Biltzeebub
Tool and mode: Claude, chat
Requested: Steps to move PROCESS.md and Verification-log.md into docs/ using the GitHub website (Lab 4 step 3), and a PR description.
Generated: A step-by-step procedure and a What/Why/How PR description. No file content was generated.
Claimed: Both files move into docs/ with history intact and no content change.
Verified: The comparison page showed 2 commits and 2 files changed, both "File renamed without changes". The merged diff has 0 lines changed.
Not verified: Whether any other file still refers to the old root paths; I did not search. [minor]
Disposition: Used the procedure and the PR description as given.

## PR #58 2026 - 11 - 11 @IvanLuu005
Requested: ChatGPT Work, a list of portions missing from M2
Generated: List of issues that have not been addressed in M2
Claimed: All M2 requirements will be fulfilled after completing the fix
Verified: docs/decisions have been fixed and are up to standard for M2
Not Verified: Other issues for M2.

## PR #43 2026 - 11 - 4 @Santie0
Requested: ChatGPT Work, code for tea catalog 
Generated: 323 lines, one test function 
Claimed: Code will show a tea catalog page with description of teas.   
Verified: Looked over code to see if it matches with what's needed in catalog & if test.py runs.  
Not verified: Whether tests pass or fails.

## PR #35 2026 - 10 - 28 @Santie0
Requested: ChatGPT Work, a mermaid diagram 
Generated: 26 lines
Claimed: Mermaid diagram of files if database.py was changed.  
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #33 2026 - 10 - 26 @Santie0
Requested: ChatGPT Work, a mermaid diagram 
Generated: 26 lines
Claimed: Mermaid diagram created based off code. 
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #32 2026 - 10 - 21 @Zairah-Haque
Requested: ChatGPT Work, a sequence diagram 
Generated: 72 lines
Claimed: Both mermaid and Sequence diagram merged into Architecture.md to show costumer interaction flow and function/class interactions. 
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #31 2026 - 10 - 21 @Zairah-Haque
Requested: ChatGPT Work, a sequence diagram 
Generated: 26 lines
Claimed: Sequence diagram to show customer interaction flow. 
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #30 2026-10-19 @Zairah-Haque
Requested: ChatGPT Work, a mermaid diagram 
Generated: 36 lines
Claimed: Mermaid diagram created from use cases. 
Verified: Looked over diagram and slides to see if it corresponds. 
Not verified: N/A

## PR #12 2026-09-23 @kekoavan
Requested: ChatGPT Work, a pytest test for viewing tea information. 
Generated: 23 lines, one test function
Claimed: Customers can view tea name, description, and price at /teas. 
Verified: Ran it, code and test files were created and inspected.
Not verified: Whether the pytest test passes [minor]

## PR #7 2026-09-23 @Santie0 
Requested: ChatGPT Work, a pytest test for the shipping page
Generated: 8 lines, one test function
Claimed: Fails now, passes once the shipping page displays the customer’s cart
Verified: ran it. Fails with AssertionError because the shipping page is not implemented.
Not verified: That the client fixture, /shipping route, and session format match the implementation [moderate]

## PR #10 2026-09-23 @Zairah-Haque
Requested : ChatGPT Work . A pytest test for adding selected tea to cart .
Generated : 6 lines. One test function .
Claimed : Test is running and pytest has configured. Has buttons that display "add to cart" and "Cart". And cart displays "selected tea". 
Verified : All displayed buttons can be clicked. 
Not verified : user can not select an actual tea. [ severe ]

## PR #14 2026-09-23 @IvanLuu005
Requested: ChatGPT Work, A pytest for removing selected tea from cart.
Generated: 9 lines, one test function
Claimed: Fails until the tea catalog compiler and primary tea typologies exist.
Verified: Test runs and passes
Not Verified: Test execution and integration. [major]

## Issue #13 (class exercise, no PR) 2026-09-23 @Biltzeebub
Tool and mode: Claude, Cowork
Requested: One pytest test for "Compile Tea Catalog and Typology" — teas sorted by type, then harvest year, then price per gram — that fails today and passes once built.
Generated: One fixture (in-memory DB, 3 seeded teas), one test function. 34 lines.
Claimed: get_catalog() returns teas ordered by type, then harvest_year, then price_per_gram.
Verified: Not run.
Not verified: whether the test executes at all — app.database and app.catalog don't exist yet, so it may fail on import before ever reaching the assertion. [moderate]
Disposition: Not committed; the test is not in the repo.
