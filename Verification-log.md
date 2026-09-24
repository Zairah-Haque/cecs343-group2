PR #18 2026-09-23 @Biltzeebub
Requested: One pytest test for "Compile Tea Catalog and Typology" — teas sorted by type, then harvest year, then price per gram — that fails today and passes once built.
Generated: One fixture (in-memory DB, 3 seeded teas), one test function. 34 lines.
Claimed: get_catalog() returns teas ordered by type, then harvest_year, then price_per_gram.
Verified: Not run.
Not verified: whether the test executes at all — app.database and app.catalog don't exist yet, so it may fail on import before ever reaching the assertion. [moderate]

## PR #12 2026-09-23 @IvanLuu005
Requested: ChatGPT Work, A pytest for removing selected tea from cart.
Generated: 9 lines, one test function
Claimed: Fails until the tea catalog compiler and primary tea typologies exist.
Verified: Test runs and passes
Not Verified: Test execution and integration. [major]

## PR #11 2026-09-23 @Zairah-Haque
Requested : ChatGPT Work . A pytest test for adding selected tea to cart .
Generated : 6 lines. One test function .
Claimed : Test is running and pytest has configured. Has buttons that display "add to cart" and "Cart". And cart displays "selected tea". 
Verified : All displayed buttons can be clicked. 
Not verified : user can not select an actual tea. [ severe ]

## PR #8 2026-09-23 @Santie0 
Requested: ChatGPT Work, a pytest test for the shipping page
Generated: 8 lines, one test function
Claimed: Fails now, passes once the shipping page displays the customer’s cart
Verified: ran it. Fails with AssertionError because the shipping page is not implemented.
Not verified: That the client fixture, /shipping route, and session format match the implementation [moderate]
