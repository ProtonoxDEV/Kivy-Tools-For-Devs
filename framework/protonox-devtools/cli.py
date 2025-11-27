"""Command line interface entrypoint for `protonox` command."""

import argparse

from . import doctor, project_templates


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="protonox", description="Protonox developer tools")
    parser.add_argument("command", choices=["doctor", "template"], help="Command to run")
    parser.add_argument("name", nargs="?", help="Template name")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "doctor":
        doctor.run_checks()
    elif args.command == "template":
        project_templates.create(args.name or "default")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
