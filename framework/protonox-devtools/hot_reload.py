"""Hot reload utilities for Protonox apps."""

import importlib
from pathlib import Path
from typing import Iterable


def reload_modules(modules: Iterable[str]) -> None:
    for module_name in modules:
        if module_name in list(importlib.sys.modules.keys()):
            importlib.reload(importlib.import_module(module_name))


def watch_and_reload(paths: Iterable[Path], on_reload=None) -> None:
    for path in paths:
        if on_reload:
            on_reload(path)
