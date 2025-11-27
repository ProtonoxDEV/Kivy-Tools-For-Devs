from __future__ import annotations

import importlib
import logging
from pathlib import Path
from typing import Callable

from watcher import PollingWatcher

logger = logging.getLogger("protonox.hot_reload")


def reload_module(target: str) -> None:
    try:
        importlib.invalidate_caches()
        importlib.reload(importlib.import_module(target))
        logger.info("Reloaded module: %s", target)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Hot reload failed for %s: %%s", target, exc)


def watch_and_reload(paths: list[str], on_reload: Callable[[Path], None] | None = None) -> None:
    watcher = PollingWatcher(paths, interval=1.0)

    def _handle(path: Path) -> None:
        logger.info("Detected change: %s", path)
        if on_reload:
            on_reload(path)

    watcher.start(_handle)
