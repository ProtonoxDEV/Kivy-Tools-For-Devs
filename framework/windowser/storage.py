"""Storage utilities for Protonox apps."""

import os
from pathlib import Path
from typing import Optional


APP_DATA_DIR = Path(os.environ.get("PROTONOX_APP_DATA", Path.home() / ".protonox"))


def ensure_app_data(subdir: Optional[str] = None) -> Path:
    base = APP_DATA_DIR
    if subdir:
        base = base / subdir
    base.mkdir(parents=True, exist_ok=True)
    return base
