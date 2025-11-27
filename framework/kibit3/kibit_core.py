"""Core entrypoints for kibit3 integration."""

from dataclasses import dataclass
from typing import Iterable

from .text_renderer import layout_text, select_font


@dataclass
class RenderedGlyph:
    glyph: str
    font: str


def render_text(text: str) -> Iterable[RenderedGlyph]:
    for glyph in layout_text(text):
        yield RenderedGlyph(glyph=glyph, font=select_font(glyph))
