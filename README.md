# Supply Co-usage Insight

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/azw584hseh/badge.svg)](https://ask.thili.ai/b/azw584hseh)

This project, 'Supply Co-usage Insight', analyzes medical procedure data to find which supplies are frequently used together. It uses frequent itemset mining to identify strong co-occurring medical supply sets, providing insights for optimizing stock placement and procurement efficiency for hospital administrators.

## What you are building

**Goal.** You will build a system that analyzes mock medical procedure data to identify frequently co-occurring medical supplies, helping hospital administrators optimize stock placement and procurement efficiency.

**Done when.** The project is done when you have identified strong co-occurring medical supply sets, proven by outputting a list of frequent itemsets with their support, and generated a report of these identified supply bundles.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Create mock medical procedure data, where each procedure lists used supply SKUs.**  
      Hint: Create mock data representing medical procedures and their associated supply SKUs, similar to transaction data.
- [ ] **2. Implement frequent itemset mining (e.g., using thilimarketbasket).**  
      Hint: Apply the `lfretail-lfmarketbasket` frequent itemset mining technique.
- [ ] **3. Analyze and display the most frequent co-occurring supply itemsets.**  
      Hint: Display and interpret the most frequent itemsets found by the mining algorithm.
- [ ] **4. Compare the mined itemsets against simple baseline expectations.**  
      Hint: Establish a simple baseline for comparison, perhaps by looking at individual supply frequencies.
- [ ] **5. Generate a report of identified supply bundles.**  
      Hint: Structure your findings into a clear, concise report of the identified supply bundles.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- (none)
