# Candidate Exercise — Pair Programming
 
**What this session is**
 
This is a collaborative pair-programming exercise in Python (~60 minutes). You'll work through it *with* one of our team members — treat them as a teammate, not an examiner. We're far more interested in how you reason about an open-ended problem and how you work with someone else than in whether you produce perfect or complete code. There's no single right answer, and you are not expected to finish everything.
 
**What you're working with**
 
We'll share some starter code with three tables dumped as csv's. They were exported from different systems.
 
Hagerty serves members across several lines of business: specialty **insurance**, an online **marketplace**, the Hagerty Drivers Club **membership** (HDC, which includes the magazine), and live **events** (such as the Amelia concours). A customer might touch just one of these or several over time. Marketing wants to understand which acquisition channels bring in customers who go on to become paying customers, so they can decide where to invest next.
 
`customers`
 
| column | description |
|---|---|
| `customer_id` | customer identifier |
| `account_created_date` | when the account was first created |
| `acquisition_channel` | how they were acquired (e.g. organic, paid_search, social, agent, referral) |
| `signup_product` | the line of business they first showed interest in |
| `state` | customer's state |
 
`transactions`
 
| column | description |
|---|---|
| `customer_id` | customer identifier |
| `transaction_date` | date of the transaction |
| `product_line` | insurance, marketplace, hdc_membership, or events |
| `transaction_type` | e.g. `payment`, `refund` |
| `amount` | dollar amount |
 
A note on `amount`: for most lines this is what the customer paid. For **marketplace** transactions, `amount` is the full **vehicle sale price** — Hagerty's revenue on a marketplace sale is **7% of that**, not the whole amount.
 
`customer_attributes`
 
| column | description |
|---|---|
| `customer_id` | customer identifier |
| `vehicle_count` | number of vehicles on file |
| `top_vehicle_value` | value of the customer's most valuable vehicle (USD) |
| `vehicle_category` | e.g. classic, muscle, exotic, modern_collectible, truck_suv |
| `age_band` | customer age band |
 
**The task**
 
To start: **which acquisition channels bring in the customers most likely to become profitable paying customers?** Feel free to ask about anything that's unclear, and tell us about any assumptions you're making along the way. 

**Tools**
 
Use whatever you'd normally use, including AI assistants (Copilot, Claude, ChatGPT, etc.) and web search. We use these tools day to day and want to see how you work realistically. The only thing we ask is that you stay able to explain and build on whatever ends up on the screen — your teammate will be curious about the choices being made.
 
Talking through your thinking as you work makes this much more useful for both of us.