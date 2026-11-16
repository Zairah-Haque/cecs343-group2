## PR #13 2026-09-23 @Biltzeebub
Requested: One pytest test for "Compile Tea Catalog and Typology" — teas sorted by type, then harvest year, then price per gram — that fails today and passes once built.
Generated: One fixture (in-memory DB, 3 seeded teas), one test function. 34 lines.
Claimed: get_catalog() returns teas ordered by type, then harvest_year, then price_per_gram.
Verified: Not run.
Not verified: whether the test executes at all — app.database and app.catalog don't exist yet, so it may fail on import before ever reaching the assertion. [moderate]

## PR #14 2026-09-23 @IvanLuu005
Requested: ChatGPT Work, A pytest for removing selected tea from cart.
Generated: 9 lines, one test function
Claimed: Fails until the tea catalog compiler and primary tea typologies exist.
Verified: Test runs and passes
Not Verified: Test execution and integration. [major]

## PR #10 2026-09-23 @Zairah-Haque
Requested : ChatGPT Work . A pytest test for adding selected tea to cart .
Generated : 6 lines. One test function .
Claimed : Test is running and pytest has configured. Has buttons that display "add to cart" and "Cart". And cart displays "selected tea". 
Verified : All displayed buttons can be clicked. 
Not verified : user can not select an actual tea. [ severe ]

## PR #7 2026-09-23 @Santie0 
Requested: ChatGPT Work, a pytest test for the shipping page
Generated: 8 lines, one test function
Claimed: Fails now, passes once the shipping page displays the customer’s cart
Verified: ran it. Fails with AssertionError because the shipping page is not implemented.
Not verified: That the client fixture, /shipping route, and session format match the implementation [moderate]

## PR #12 2026-09-23 @kekoavan
Requested: ChatGPT Work, a pytest test for viewing tea information. 
Generated: 23 lines, one test function
Claimed: Customers can view tea name, description, and price at /teas. 
Verified: Ran it, code and test files were created and inspected.
Not verified: Whether the pytest test passes [minor]

## PR #30 2026-10-19 @Zairah-Haque
Requested: ChatGPT Work, a mermaid diagram 
Generated: 36 lines
Claimed: Mermaid diagram created from use cases. 
Verified: Looked over diagram and slides to see if it corresponds. 
Not verified: N/A 

## PR #31 2026 - 10 - 21 @Zairah-Haque
Requested: ChatGPT Work, a sequence diagram 
Generated: 26 lines
Claimed: Sequence diagram to show customer interaction flow. 
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #33 2026 - 10 - 26 @Santie0
Requested: ChatGPT Work, a mermaid diagram 
Generated: 26 lines
Claimed: Mermaid diagram created based off code. 
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #35 2026 - 10 - 28 @Santie0
Requested: ChatGPT Work, a mermaid diagram 
Generated: 26 lines
Claimed: Mermaid diagram of files if database.py was changed.  
Verified: Looked over diagram and slide to see if it corresponds. 
Not verified: N/A

## PR #43 2026 - 11 - 4 @Santie0
Requested: ChatGPT Work, code for tea catalog 
Generated: 323 lines, one test function 
Claimed: Code will show a tea catalog page with description of teas.   
Verified: Looked over code to see if it matches with what's needed in catalog & if test.py runs.  
Not verified: Whether tests pass or fails. 
