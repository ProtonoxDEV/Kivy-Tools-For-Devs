"""Canvas overrides to be wired into the Protonox Kivy fork."""

from typing import Iterable

from .pipeline import build_pipeline
from .render_core import RenderCommand


def inject_commands(commands: Iterable[RenderCommand]) -> Iterable[RenderCommand]:
    return build_pipeline(commands)
