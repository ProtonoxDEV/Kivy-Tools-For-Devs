from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Callable, Iterable


class PollingWatcher:
    """Minimal polling watcher to avoid external dependencies."""

    def __init__(self, paths: Iterable[str], interval: float = 1.0):
        self.paths = [Path(p) for p in paths]
        self.interval = interval
        self._mtimes: dict[str, float] = {}

    def start(self, on_change: Callable[[Path], None]) -> None:
        for path in self.paths:
            if path.exists():
                self._mtimes[str(path)] = path.stat().st_mtime
        while True:
            time.sleep(self.interval)
            for path in self.paths:
                if not path.exists():
                    continue
                mtime = path.stat().st_mtime
                key = str(path)
                if mtime != self._mtimes.get(key):
                    self._mtimes[key] = mtime
                    on_change(path)
                for root, _, files in os.walk(path):
                    for fname in files:
                        fpath = Path(root) / fname
                        key = str(fpath)
                        mtime = fpath.stat().st_mtime
                        if mtime != self._mtimes.get(key):
                            self._mtimes[key] = mtime
                            on_change(fpath)
