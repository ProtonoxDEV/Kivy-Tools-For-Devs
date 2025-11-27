"""Project template generator for Protonox."""

from pathlib import Path


def create(name: str) -> Path:
    base = Path(name)
    base.mkdir(parents=True, exist_ok=True)
    (base / "main.py").write_text("print('Hello from Protonox template')\n")
    return base
