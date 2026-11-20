"""Command-line entry point: `python -m app.cli --help`."""
from __future__ import annotations

import argparse
import json
import sys

from app import core


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="supply-co-usage-insight",
        description="For hospital administrators, analyzes which medical supplies are frequently used together across procedures, optimizing stock placement and procurement efficiency.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # Base verification command
    sub.add_parser("hello", help="check that everything is wired up")

    # Milestone 1 command: Generate mock procedure data
    gen_p = sub.add_parser("generate", help="Generate mock medical procedure data")
    gen_p.add_argument("--count", type=int, default=1000, help="Number of procedures to simulate (default: 1000)")
    gen_p.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")

    # Milestone 2 command: Mine frequent itemsets
    mine_p = sub.add_parser("mine", help="Mine frequent supply itemsets using bitset Apriori")
    mine_p.add_argument("--min-support", type=float, default=0.10, help="Minimum support threshold (default: 0.10)")
    mine_p.add_argument("--max-size", type=int, default=4, help="Maximum bundle size to mine (default: 4)")

    # Milestone 3 command: Analyze frequent co-occurring supply sets
    ana_p = sub.add_parser("analyze", help="Analyze and display top co-occurring supply sets")
    ana_p.add_argument("--min-size", type=int, default=2, help="Minimum items per bundle (default: 2)")
    ana_p.add_argument("--top-k", type=int, default=10, help="Number of top bundles to display (default: 10)")

    # Milestone 4 command: Compare against baseline expectations
    sub.add_parser("compare", help="Compare mined itemsets against independent single-item baseline")

    # Milestone 5 command: Generate procurement & stock placement report
    rep_p = sub.add_parser("report", help="Generate comprehensive hospital procurement report")
    rep_p.add_argument("--output", type=str, default=None, help="Optional custom output file path")

    args = parser.parse_args(argv)

    if args.command == "hello":
        print("Supply Co-usage Insight is ready. Open README.md for your milestones.")
    elif args.command == "generate":
        data = core.milestone_1(n=args.count, seed=args.seed)
        print(f"Generated {len(data)} mock medical procedures saved to data/procedures.json")
        sample = data[0]
        print(f"Sample procedure {sample['procedure_id']} ({sample['procedure_type']}):")
        print(f"  Supplies ({sample['supply_count']}): {', '.join(sample['supplies'])}")
    elif args.command == "mine":
        itemsets = core.milestone_2(min_support=args.min_support, max_size=args.max_size)
        print(f"Mined {len(itemsets)} frequent supply itemsets (min_support={args.min_support}):")
        for items, support in sorted(itemsets.items(), key=lambda x: -x[1])[:10]:
            print(f"  Support {support * 100:5.1f}%: {', '.join(sorted(items))}")
    elif args.command == "analyze":
        bundles = core.milestone_3(min_size=args.min_size, top_k=args.top_k)
        print(f"Top {len(bundles)} Co-occurring Medical Supply Bundles (size >= {args.min_size}):")
        for idx, b in enumerate(bundles, 1):
            print(f"[{idx:02d}] Support: {b['support_percent']} | Items: {len(b['skus'])}")
            print(f"     SKUs:  {', '.join(b['skus'])}")
            print(f"     Names: {', '.join(b['names'])}")
    elif args.command == "compare":
        comparisons = core.milestone_4()
        print(f"Baseline Comparison & Lift Analysis (top {min(10, len(comparisons))} bundles):")
        for idx, c in enumerate(comparisons[:10], 1):
            print(f"[{idx:02d}] Lift: {c['lift']:4.2f}x ({c['classification']})")
            print(f"     Observed: {c['observed_support'] * 100:.1f}% | Expected: {c['expected_support'] * 100:.1f}%")
            print(f"     SKUs:     {', '.join(c['skus'])}")
    elif args.command == "report":
        report_text = core.milestone_5()
        print(report_text)
        if args.output:
            with open(args.output, "w") as f:
                f.write(report_text)
            print(f"\nReport written to {args.output}")


if __name__ == "__main__":
    main()
