"""Background service coordination for Protonox."""

from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass
class ServiceSpec:
    name: str
    on_start: Optional[Callable[[], None]] = None
    on_stop: Optional[Callable[[], None]] = None


class ServiceRegistry:
    def __init__(self):
        self._services: Dict[str, ServiceSpec] = {}

    def register(self, spec: ServiceSpec) -> None:
        self._services[spec.name] = spec

    def start(self, name: str) -> None:
        spec = self._services.get(name)
        if spec and spec.on_start:
            spec.on_start()

    def stop(self, name: str) -> None:
        spec = self._services.get(name)
        if spec and spec.on_stop:
            spec.on_stop()
