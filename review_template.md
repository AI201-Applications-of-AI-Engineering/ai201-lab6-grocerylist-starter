# Code Review Notes

Fill this in as you work through the milestones. Each section mirrors the structure of a real GitHub pull request review.

---

## PR #1 — Bulk Purchase (`pr1_bulk_purchase.py`)

### Summary
*What does this PR do? (1–2 sentences in your own words)*
    The code should purchase all unpurchased items in the list, setting "is_purchased" to "true". Each of the item's "purchased_by" is set to the requesting user, and "purchased_at" set to now. Response should return the count of items that were purchased by this call.
>

### Issues

For each issue you find, note: where it is (file + function), what's wrong, and why it matters in production.

**Issue 1**
- Location: http://127.0.0.1:5000/lists/LIST_ID/items
- What's wrong: The code overwrites "purchased_by" with each call.
- Why it matters: If the buyer was previously "leo" and the new user is maya, the call replaces all the "purchased_by" with the new user, maya. However, if we call it again, this time with no user, all the previous "purchased_by" that was set to maya before is now set to "".
- Suggested fix: implement error-fixing, making sure that the call doesn't overwrite previously bought items. 

**Issue 2**
- Location: purchased_all_items
- What's wrong: it returns all the items in the list, rather than unpurchased one
- Why it matters: Because it returns all items, it doesn't take into account items that were already purchased. The already purchased_items are overwritten with the new buyer, which means the already purchased_items now have new "purchased_by" owners.
- Suggested fix:

**Issue 3** *(if found)*
- Location: http://127.0.0.1:5000/lists/LIST_ID/items
- What's wrong: No user validation
- Why it matters: If we have "maya" buy all the unpurchased items, the "purchased_by" is set to "maya", which is right. However, if we call the function again, this time with "", or no user, then it will rewrite the user with the no user.
- Suggested fix: Implement user validation. We want to make sure that the IDs are valid, so that they are actually being purchased by existing users.

### Questions for the Author
*Things you're uncertain about — design choices that could be intentional or bugs depending on intent.*

> Not sure, most of these issues are just bugs of the functionalities, not actual design problems.

### Verdict
- [ ] Approve — ship it
- [x] Request Changes — needs fixes before merging
- [ ] Comment — needs discussion before a verdict

**Rationale** *(1–2 sentences)*:

> While the author wanted the function to purchase all of the unpurchased items, it currently has 3 errors. 1: it iterates over the entire list, regardless of "purchased_by". 2: it overwrites "purchased_by", even if it was previously purchased. 3: it never verified if the user existed. All 3 of these can be edited and fixed.

---

## PR #2 — List Stats (`pr2_list_stats.py`)

### Summary
*What does this PR do? (1–2 sentences in your own words)*

>

### Issues

**Issue 1**
- Location: get_list_stats
- What's wrong: by_category is storing all items, not unpurchased ones
- Why it matters: The frontend team wanted categories of the UNPURCHASED items, but because we used "items" which is what was returned by the query, we got ALL the items rather than filtering by unpurchased ones.
- Suggested fix: Since "items" is from the query, we can use a for loop filtering only items where "item.is_purchased" returns false or null. This way, we only get items that are not purchased, and replace the for loop with this group instead of "items".

**Issue 2**
- Location: get_list_stats
- What's wrong: The return returns "by_category", but "by_category" matches "purchased" rather than "remaining".
- Why it matters: The frontend team wanted a stats endpoint that shows the remaining in cart. This means that it wants the "by_category" to show the remaining amount, not the total amount.
- Suggested fix: Fix the for loop, using a counter from 0 to "remaining" and only accessing items that are not purchased. 

**Issue 3** *(if found)*
- Location: http://127.0.0.1:5000/lists/list_id/stats
- What's wrong: list doesn't exist, but still passes HTTP protocols
- Why it matters: Even though we had a non-existent list, we still returned status code 200, meaning it passed. In the long run, this will cause a lot of false positives, where we think it is an actual list, but is actually non-existent.
- Suggested fix: Implement code handling whether the list exists or not.

### Questions for the Author
*A good code review often surfaces design questions, not just bugs. What would you want to clarify before approving?*

>

### Verdict
- [ ] Approve — ship it
- [x] Request Changes — needs fixes before merging
- [ ] Comment — needs discussion before a verdict

**Rationale** *(1–2 sentences)*:

> The issues are mostly just bugs, not actual design issues. 

---

## Reflection

*Answer after completing both reviews.*

**1.** Which issue was hardest to spot, and why?
The GET error (false positive) and category returning total amount rather than remaining amount. Because the GET error didn't check if the list existed or not, the false positive will run no matter what. This means that if we didn't test for the false positive, it became a lot harder to find when it actually passes production. The category one falls into the same loophole; if we didn't run sample tests, it becomes very hard to notice.
>

**2.** Which issues do you think an LLM reviewer (like Claude reviewing its own code) would most likely miss? Why?
Ignoring existing state, return count meaning something different from its claim, and no existing/authorization checks. While the individual version had the error-handling,the AI writing the code in bulk ignores this portion, and skips past it, resulting in overwriting existing states. Bulk operations seem to make the AI skip a lot of the single-item functionalities/checks, resulting in the incomplete work.
>

**3.** One thing you'd add to a code review checklist for AI-generated backend code:
    Check for edge cases; specifically, making sure that the variables are right.
>
