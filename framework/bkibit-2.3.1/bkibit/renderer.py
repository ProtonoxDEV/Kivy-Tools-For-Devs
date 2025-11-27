"""Minimal renderer stub for Protonox."""

from __future__ import annotations

import logging
from typing import List

logger = logging.getLogger("protonox.bkibit")


class Renderer:
    def __init__(self) -> None:
        self.queue: List[dict] = []

    def enqueue(self, instruction: dict) -> None:
        logger.debug("Enqueue render instruction: %s", instruction)
        self.queue.append(instruction)

    def render(self) -> None:
        logger.info("Rendering %d instructions", len(self.queue))
        for instr in sorted(self.queue, key=lambda i: i.get("order", 0)):
            logger.debug("Render instruction: %s", instr)
        self.queue.clear()
