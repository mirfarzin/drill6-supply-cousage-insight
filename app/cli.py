"""Command-line entry point: `python -m app.cli --help`."""
import argparse


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="supply-co-usage-insight", description="For hospital administrators, analyzes which medical supplies are frequently used together across procedures, optimizing stock placement and procurement efficiency.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("hello", help="check that everything is wired up")
    # TODO: add your own commands here as you work through the milestones.
    args = parser.parse_args(argv)
    if args.command == "hello":
        print("Supply Co-usage Insight is ready. Open README.md for your milestones.")


if __name__ == "__main__":
    main()
