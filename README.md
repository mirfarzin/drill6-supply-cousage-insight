# Supply Co-usage Insight

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/azw584hseh/badge.svg)](https://ask.thili.ai/b/azw584hseh)

This project, 'Supply Co-usage Insight', analyzes medical procedure data to find which supplies are frequently used together. It uses frequent itemset mining (bitset Apriori via `thilimarketbasket`) to identify strong co-occurring medical supply sets, providing insights for optimizing stock placement and procurement efficiency for hospital administrators.

## What you are building

**Goal.** You will build a system that analyzes mock medical procedure data to identify frequently co-occurring medical supplies, helping hospital administrators optimize stock placement and procurement efficiency.

**Done when.** The project is done when you have identified strong co-occurring medical supply sets, proven by outputting a list of frequent itemsets with their support, and generated a report of these identified supply bundles.

## Milestones

- [x] **1. Create mock medical procedure data, where each procedure lists used supply SKUs.**  
      *Implemented in `app/core.py:generate_mock_procedure_data` and CLI command `python -m app.cli generate`.*
- [x] **2. Implement frequent itemset mining (e.g., using thilimarketbasket).**  
      *Implemented in `app/core.py:run_frequent_itemset_mining` using bitset Apriori with support monotonicity and CLI command `python -m app.cli mine`.*
- [x] **3. Analyze and display the most frequent co-occurring supply itemsets.**  
      *Implemented in `app/core.py:analyze_frequent_bundles` and CLI command `python -m app.cli analyze`.*
- [x] **4. Compare the mined itemsets against simple baseline expectations.**  
      *Implemented in `app/core.py:compare_against_baseline` calculating statistical independence baselines and synergy Lift ($>1.5\times$).*
- [x] **5. Generate a report of identified supply bundles.**  
      *Implemented in `app/core.py:generate_procurement_report` and CLI command `python -m app.cli report` outputting physical placement and procurement recommendations.*

## Run it

Requires Python 3.12+ (or 3.13) and git.

```bash
python -m venv .venv
# On Linux/macOS: source .venv/bin/activate
# On Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env

# Verify installation
python -m app.cli hello

# Milestone workflows
python -m app.cli generate --count 1000
python -m app.cli mine --min-support 0.10
python -m app.cli analyze --min-size 2 --top-k 10
python -m app.cli compare
python -m app.cli report

# Run unit tests
pytest -v
```

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.**
