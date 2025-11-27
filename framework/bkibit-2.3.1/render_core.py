"""Core rendering hooks replacing selected Kivy canvas stages."""

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class RenderCommand:
    opcode: str
    args: List[float]


def compile_commands(commands: Iterable[RenderCommand]) -> List[RenderCommand]:
    return [cmd for cmd in commands]
