"""Command line entrypoint.

Acceptance trace: AC-001, AC-002, AC-003.
"""
from __future__ import annotations
import argparse
import yaml
from .audit import audit_repository
from .seeding import seed_target
from .validation import validate_target
from .detection import detect_mode
from .landscape import generate_landscape
from .reconciliation import generate_reconciliation_report

def main(argv: list[str] | None = None) -> int:
    parser=argparse.ArgumentParser(prog="product-harness"); sub=parser.add_subparsers(dest="command", required=True)
    boot=sub.add_parser("bootstrap"); boot.add_argument("target", nargs="?", default="."); boot.add_argument("--mode", default="auto"); boot.add_argument("--include", action="append"); boot.add_argument("--exclude", action="append")
    valid=sub.add_parser("validate"); valid.add_argument("target", nargs="?", default=".")
    detect=sub.add_parser("detect"); detect.add_argument("target", nargs="?", default="."); detect.add_argument("--mode", default="auto")
    landscape=sub.add_parser("landscape", help="Generate a product idea landscape"); landscape.add_argument("target", nargs="?", default="."); landscape.add_argument("--stale-after-days", type=int, default=30)
    reconcile=sub.add_parser("reconcile", help="Generate a product consistency report"); reconcile.add_argument("target", nargs="?", default="."); reconcile.add_argument("--record")
    audit=sub.add_parser("audit", help="Reconstruct current product evidence and preserve audit history"); audit.add_argument("target", nargs="?", default=".")
    args=parser.parse_args(argv)
    if args.command == "detect":
        result=detect_mode(args.target,args.mode); print(f"{result.mode} ({result.status}): {'; '.join(result.evidence)}"); return 0
    if args.command == "bootstrap":
        report=seed_target(args.target,args.mode,args.include,args.exclude); print(f"Mode: {report.mode} ({report.status})"); print("Created:", *report.created, sep="\n- "); print("Preserved:", *report.preserved, sep="\n- "); errors=validate_target(args.target)
        if errors:
            print("Validation failed:", *[f"- {e}" for e in errors], sep="\n"); return 1
        print("Validation passed. Recommended next command: $product-audit" if report.mode == "brownfield" else "Validation passed. Recommended next command: $product-talk"); return 0
    if args.command == "landscape":
        try:
            report = generate_landscape(args.target, args.stale_after_days)
        except ValueError as exc:
            print(f"ERROR: {exc}")
            return 1
        print(f"Landscape: {report.path}")
        print(f"Records: {report.record_count}; require review: {report.stale_count}; missing documents: {report.missing_document_count}")
        return 0
    if args.command == "reconcile":
        try:
            report = generate_reconciliation_report(args.target, args.record)
        except ValueError as exc:
            print(f"ERROR: {exc}")
            return 1
        print(f"Reconciliation report: {report.path}")
        print(f"Records: {report.record_count}; proposed relations: {report.proposed_count}; alignment reviews: {report.needs_review_count}")
        return 0
    if args.command == "audit":
        try:
            report = audit_repository(args.target)
        except (OSError, yaml.YAMLError) as exc:
            print(f"ERROR: {exc}")
            return 1
        print(f"Current feature inventory: {report.feature_inventory_path}")
        print(f"Repository map: {report.repository_map_path}")
        print(f"Historical audit report: {report.historical_report_path}")
        print(f"Audit history index: {report.index_path}")
        print("Recommended next focus: $product-review-current-state")
        return 0
    errors=validate_target(args.target)
    if errors: print(*[f"ERROR: {e}" for e in errors], sep="\n"); return 1
    print("Product Discovery Harness validation passed."); return 0

if __name__ == "__main__": raise SystemExit(main())
