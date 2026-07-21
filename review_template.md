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

>

### Verdict
- [ ] Approve — ship it
- [ ] Request Changes — needs fixes before merging
- [ ] Comment — needs discussion before a verdict

**Rationale** *(1–2 sentences)*:

>

---

## PR #2 — List Stats (`pr2_list_stats.py`)

### Summary
*What does this PR do? (1–2 sentences in your own words)*

>

### Issues

**Issue 1**
- Location:
- What's wrong:
- Why it matters:
- Suggested fix:

**Issue 2**
- Location:
- What's wrong:
- Why it matters:
- Suggested fix:

**Issue 3** *(if found)*
- Location:
- What's wrong:
- Why it matters:
- Suggested fix:

### Questions for the Author
*A good code review often surfaces design questions, not just bugs. What would you want to clarify before approving?*

>

### Verdict
- [ ] Approve — ship it
- [ ] Request Changes — needs fixes before merging
- [ ] Comment — needs discussion before a verdict

**Rationale** *(1–2 sentences)*:

>

---

## Reflection

*Answer after completing both reviews.*

**1.** Which issue was hardest to spot, and why?

>

**2.** Which issues do you think an LLM reviewer (like Claude reviewing its own code) would most likely miss? Why?

>

**3.** One thing you'd add to a code review checklist for AI-generated backend code:

>
