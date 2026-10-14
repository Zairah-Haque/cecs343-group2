# Requirements

## Purpose
Created for customers who are looking to buy tea from merchants who sell them via the website. This eliminates physical limitations of distance, availability, and logistics while reaching a larger customer base. 

## Actors
1. Customer
2. Shop Owner/Seller
3. Sales Staff
4. Logistics Staff

## Functional

#7 creating a shipping page
#8 creating a display page for teas available 
#10 adding tea to cart 
#13 Compile tea catalogue and typology 
#14 Tea removed from cart
    

## Quality

### Q1. Catalog page responds quickly (#18)
- **Number:** the first screen of the tea catalog page appears within 2 seconds
- **Measured over:** 95% of catalog page requests
- **Conditions:** up to 100 simultaneous users
- **Where the number came from:** [one clause]
- **Owner:** @kekoavan

### Q2. Stored passwords cannot be read (#20)
- **Number:** 0 customer passwords stored in readable form
- **Measured over:** 100% of stored customer passwords
- **Conditions:** inspection of the database and of its backups
- **Where the number came from:** [one clause]
- **Owner:** @kekoavan

### Q3. No duplicate orders (#19)
- **Number:** exactly 1 order created in each of the 100 tests (100 of 100 must pass)
- **Measured over:** 100 consecutive repeated-submission tests
- **Conditions:** [N] clicks on the checkout button within [S] seconds
- **Where the number came from:** [one clause]
- **Owner:** @kekoavan

Not written yet

## Out of scope
What a reader would otherwise assume you are building.

Not written yet

## Open questions
Each with a question, an owner, a date, and a default.

Owner: Shop Owner
Date: 10/14/2026
Default: Show categories and typology; omit search and filters.
How should customers browse the tea catalog: by category, typology, search, or filters?

Owner: Shop Owner
Date: 10/14/2026
Default: Keep it in the cart and show that it is unavailable before checkout.
How should the site handle a tea that becomes unavailable while it is in a customer’s cart?

