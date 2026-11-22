## PR #80 2026 - 11 - 21 @Santie0
Tool: ChatGPT, Work
Requested: Code testing the shipping page based off of Issue #7 acceptance criteria.  
Generated: 95 lines
Claimed: Generated code that tests the shipping page based off of Issue #7 acceptance criteria. 
Verified: Ran pytest of generated code, once with old app.py code and a second time with revised app.py code. First time, 4 tests failed with Assertation Error. Second time, all tests passed.    
Not verified: Whether code will run on a new codespace. [minor] 
Disposition: Accepted after reviews from group members. 

## PR #77 2026 - 11 - 21 @Santie0
Tool: ChatGPT, Work
Requested: Revised code to fix failures for tests for catalog and shipping page. 
Generated: 306 lines
Claimed: Generated revised code that addressed failures in the test code for catalog and shipping page. 
Verified: Ran pytest of catalog and shipping page tests with newly revised code. All of the tests passed.   
Not verified: Whether code will run on a new codespace. [minor] 
Disposition: Accepted after reviews from group members. 

## PR #73 2026-11-19 @Biltzeebub
Tool and mode: Claude, chat
Requested: Exact wording to update the PR #64 log entry after a fresh-Codespace test on main, and the log entry for this PR.
Generated: Two line edits to the #64 entry (Verified: appended the 2026-11-19 Codespace result; Not verified: narrowed to release/0.9) and this entry.
Claimed: The edits record only what I ran: fresh Codespace on main, README commands, pytest passed, and /, /teas and /cart loaded.
Verified: I ran the Codespace test myself on 2026-11-19. The devcontainer installs requirements.txt on creation (read from .devcontainer/devcontainer.json). The Files changed tab shows only the two #64 lines and this new entry.
Not verified: The pytest test count (I saw the 100% progress marker, not "1 passed"). A fresh Codespace on release/0.9, which does not exist yet. [minor]
Disposition: Accepted as drafted.

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

## PR #69 2026 - 11 - 16 @Santie0
Tool: ChatGPT, Work
Requested: Tasks left to do for the completion of M3 and M4. 
Generated: 22 lines
Claimed: Generate table with the tasks that are left to do to complete the criteria for M3 and M4. 
Verified: Looked at tasks generated to see if it corresponds with the cirterias needed for M3 and M4.  
Not verified: Whether there are other tasks missing in the table. [minor] 
Disposition: Accepted as drafted. 

## PR #64 2026-11-15 @Biltzeebub
Tool and mode: Claude, chat
Requested: README run and test commands, so a fresh Codespace can start the app and run the tests using only the README (M3 requirement).
Generated: A "Running" and a "Testing" section for README.md, about 20 lines: pip install -r requirements.txt, cd tea-catalog-code, flask --app app run, the local URL, and pytest.
Claimed: Running those commands from the repository root starts the app and runs the tests.
Verified: The committed text is identical to the draft (checked against the diff). The commands were run on a scratch copy of the repo (pytest: 1 passed; /, /teas and /cart returned HTTP 200), and I ran them in a fresh Codespace on the PR branch, where they passed. Fresh Codespace on main, 2026-11-19: pytest passed; the app loaded at /, /teas and /cart using the README commands.
Not verified: A fresh Codespace on release/0.9 (the branch does not exist yet). [minor]
Disposition: Accepted as drafted, no edits.

## PR #63 2026 - 11 - 15 @Santie0
No AI on PR #63

## PR #62 2026 - 11 - 15 @Santie0
No AI on PR #62

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

## PR #55 2026 - 11 - 16 @Santie0
Tool: ChatGPT, Work
Requested: Code to test tea catalog page
Generated: 114 lines
Claimed: Code will test the tea catalog page according to the acceptance criteria of Issue #8. 
Verified: Looked to see if code corresponds with what's written for the acceptance criteria of Issue #8. Ran confest.py to see if it works, 2 tests failed with AssertationError and 5 tests passed. 
Not verified: Whether code runs on a new codespace in Github and what caused the 2 tests to fail. [moderate]
Disposition: Accepted after other members looked over it. 

## PR #43 2026 - 11 - 4 @Santie0
Tool: ChatGPT, Work
Requested: Code for tea catalog  
Generated: 323 lines, one test function 
Claimed: Code will show tea catalog once ran, along with working implementations for other functions of the shop.   
Verified: Looked over code to see if it matches with what's needed in catalog. Ran the test function to see whether it passes or fails the test. 
Not verified: Whether code runs on a new codespace in Github. [moderate]
Disposition: Accepted after other members looked over it. 

## PR #35 2026 - 10 - 28 @Santie0
Tool: ChatGPT, Work
Requested: Decision of copying Tea object's detail, along with the because, rejecteds, and costs. And a mermaid diagram for separating database.py into a different file. 
Generated: 26 lines
Claimed: A decision that would fix a problem that might occur down the line and it's reasons, costs, and why other decisions were rejected. And a Mermaid diagram of how files would change if database.py is separated. 
Verified: Looked over previous mermaid diagrams to see if new diagram changes files that are on the previous diagram. Checked if mermaid diagram renders. 
Not verified: Did not check whether the implementation copies every Tea field. And did not verify the estimate about files changed for a future edit. [moderate]
Disposition: Accepted as drafted.  

## PR #33 2026 - 10 - 26 @Santie0
Tool: ChatGPT, Work
Requested: Two mermaid diagram, one showing the classes needed and it's inheritance type. A second diagram showing the implementations for each class. And a table ranking how many times a file is imported. 
Generated: 101 lines
Claimed: Two mermaid diagrams, one diagram showing the classes and it's inheritance needed for the shop. A second one showing the implementations for each class. And a table showing the number of imports a file has, and the amount of files that import it.  
Verified: Looked over diagram to see if it has everything listed for what's needed in the shop. And compared the number of files imported on the table with the diagram created. Checked if mermaid diagram renders. 
Not verified: Did not confirm the ranking against the code. [moderate] 
Disposition: Accepted as drafted. 

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
Tool: ChatGPT, Work 
Requested: A pytest test for the shipping page
Generated: 8 lines, one test function
Claimed: Fails now, passes once the shipping page displays the customer’s cart
Verified: Ran it. Fails with AssertionError because the shipping page is not implemented.
Not verified: That the client fixture, /shipping route, and session format match the implementation [moderate]
Disposition: Rejected after running and failing. 

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
