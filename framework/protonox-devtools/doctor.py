"""Environment checker for Protonox projects."""

import sys


REQUIRED_TOOLS = ["python3", "buildozer", "git"]


def run_checks() -> None:
    missing = [tool for tool in REQUIRED_TOOLS if not _is_available(tool)]
    if missing:
        sys.stdout.write(f"Missing tools: {', '.join(missing)}\n")
    else:
        sys.stdout.write("Environment looks ready for Protonox development.\n")


def _is_available(binary: str) -> bool:
    from shutil import which
    return which(binary) is not None
