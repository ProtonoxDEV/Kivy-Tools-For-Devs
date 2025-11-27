"""Filesystem watcher placeholder."""

from pathlib import Path
from typing import Callable, Iterable


def simple_watch(paths: Iterable[Path], callback: Callable[[Path], None]) -> None:
    for path in paths:
        callback(path)
