"""Unit tests for Supply Co-usage Insight milestones.

Each milestone has a dedicated test verifying functionality, algorithmic soundness,
and contract adherence.
"""
from pathlib import Path
import pytest

from app import core


def test_milestone_1():
    """Milestone 1: Verify mock medical procedure transaction data generation."""
    data = core.milestone_1(n=250, seed=123)
    assert len(data) == 250
    assert Path("data/procedures.json").exists()

    # Check schema of records
    first = data[0]
    assert "procedure_id" in first
    assert "procedure_type" in first
    assert "supplies" in first
    assert "supply_count" in first
    assert isinstance(first["supplies"], list)
    assert len(first["supplies"]) >= 2

    # Verify supplies exist in the medical catalog
    for sku in first["supplies"]:
        assert sku in core.SUPPLY_CATALOG


def test_milestone_2():
    """Milestone 2: Verify frequent itemset mining on procedure supplies."""
    # Ensure dataset is generated first
    core.milestone_1(n=300, seed=42)
    itemsets = core.milestone_2(min_support=0.08, max_size=4)

    assert isinstance(itemsets, dict)
    assert len(itemsets) > 0

    # Verify all itemsets satisfy min_support and have valid frozenset keys
    for itemset, support in itemsets.items():
        assert isinstance(itemset, frozenset)
        assert support >= 0.08
        assert len(itemset) <= 4

    # Verify Apriori monotonicity: support of any subset must be >= support of superset
    for itemset, support in itemsets.items():
        if len(itemset) > 1:
            for item in itemset:
                subset = itemset - {item}
                if subset in itemsets:
                    assert itemsets[subset] >= support - 1e-6


def test_milestone_3():
    """Milestone 3: Verify analysis and display of co-occurring supply itemsets."""
    core.milestone_1(n=300, seed=42)
    bundles = core.milestone_3(min_size=2, top_k=8)

    assert isinstance(bundles, list)
    assert len(bundles) <= 8
    assert len(bundles) > 0

    prev_support = 1.0
    for b in bundles:
        assert b["bundle_size"] >= 2
        assert len(b["skus"]) == b["bundle_size"]
        assert len(b["names"]) == b["bundle_size"]
        assert "support" in b
        assert "support_percent" in b
        # Verify descending sort by support
        assert b["support"] <= prev_support + 1e-6
        prev_support = b["support"]


def test_milestone_4():
    """Milestone 4: Verify comparison against single-item baseline expectations."""
    core.milestone_1(n=300, seed=42)
    comparisons = core.milestone_4()

    assert isinstance(comparisons, list)
    assert len(comparisons) > 0

    first = comparisons[0]
    assert "skus" in first
    assert "observed_support" in first
    assert "expected_support" in first
    assert "lift" in first
    assert "classification" in first
    assert first["lift"] >= 0

    # High synergy bundles should have lift significantly above 1.0
    high_lift = [c for c in comparisons if c["classification"] == "High Procedural Synergy"]
    assert len(high_lift) > 0
    assert high_lift[0]["lift"] >= 1.5


def test_milestone_5():
    """Milestone 5: Verify report generation of identified supply bundles."""
    report = core.milestone_5()

    assert isinstance(report, str)
    assert len(report) > 200
    assert Path("data/supply_report.txt").exists()

    # Verify report sections
    assert "HOSPITAL SUPPLY CO-USAGE" in report
    assert "EXECUTIVE SUMMARY" in report
    assert "TOP CO-OCCURRING SUPPLY BUNDLES" in report
    assert "PROCEDURAL SYNERGY VS. COMMODITY CO-OCCURRENCE" in report
    assert "RECOMMENDATIONS FOR HOSPITAL ADMINISTRATORS" in report
