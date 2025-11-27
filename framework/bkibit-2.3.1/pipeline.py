"""Render pipeline integrating with Protonox Kivy."""

from typing import Iterable

from .render_core import RenderCommand, compile_commands


def build_pipeline(commands: Iterable[RenderCommand]) -> Iterable[RenderCommand]:
    compiled = compile_commands(commands)
    for command in compiled:
        yield command
