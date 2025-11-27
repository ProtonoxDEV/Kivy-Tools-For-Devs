"""Renderer hooks used by Protonox Kivy."""

from typing import Iterable

from .emoji_engine import tokenize_emojis, uses_fallback_font
from .unicode_parser import normalize_whitespace


def layout_text(text: str) -> Iterable[str]:
    cleaned = normalize_whitespace(text)
    for glyph in tokenize_emojis(cleaned):
        yield glyph


def select_font(glyph: str) -> str:
    return "kibit3-fallback" if uses_fallback_font(glyph) else "default"
