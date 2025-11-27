"""Simple registry for Python↔Java bridge callbacks."""

from typing import Callable, Dict, Optional


class Bridge:
    def __init__(self):
        self._callbacks: Dict[str, Callable[..., None]] = {}

    def register(self, name: str, callback: Callable[..., None]) -> None:
        self._callbacks[name] = callback

    def dispatch(self, name: str, *args, **kwargs) -> Optional[object]:
        callback = self._callbacks.get(name)
        if callback:
            return callback(*args, **kwargs)
        return None
