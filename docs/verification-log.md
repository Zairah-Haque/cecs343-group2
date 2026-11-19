## PR #70 2026-11-19 @Biltzeebub
Requested: Claude (chat, single prompt), reorder the 12 existing log entries newest first and return the full file text to paste.
Generated: The 12 entries in new order with blank lines normalized, no entry text added or removed.
Claimed: Only the order and the spacing between entries changed; entry wording is unchanged.
Verified: Compared the Files changed view: each of the 12 entries appears once removed and once added, and #58 is first, #13 last.
Not verified: Character-by-character match of entry wording, because the pasted text was not diffed with a tool. [minor]
Disposition: Accepted after the Files changed comparison.

## PR #64 2026-11-19 @Biltzeebub
Tool and mode: Claude, chat
Requested: Draft Verification Log entries for PRs #59 and #64 from the repo history and earlier chats.
Generated: Two entries, about 16 lines.
Claimed: Each entry matches what its PR changed and how it was checked.
Verified: Compared each entry against its PR's Files changed tab: #59 is two renames with 0 lines changed, #64 is README +20/-2.
Not verified: Whether the Verified lines of #59 and #64 describe exactly what I did, beyond the Codespace run. [minor]
Disposition: Accepted after editing the Verified and Disposition lines to match what I did.

## PR #59 2026-11-19 @Biltzeebub
Tool and mode: Claude, chat
Requested: Draft Verification Log entries for PRs #59 and #64 from the repo history and earlier chats.
Generated: Two entries, about 16 lines.
Claimed: Each entry matches what its PR changed and how it was checked.
Verified: Compared each entry against its PR's Files changed tab: #59 is two renames with 0 lines changed, #64 is README +20/-2.
Not verified: Whether the Verified lines of #59 and #64 describe exactly what I did, beyond the Codespace run. [minor]
Disposition: Accepted after editing the Verified and Disposition lines to match what I did.

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
Verified: Test runs and
