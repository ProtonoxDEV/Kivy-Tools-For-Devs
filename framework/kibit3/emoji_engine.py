"""Minimal emoji pipeline placeholder for Protonox Kivy."""

from typing import List

EMOJI_FALLBACK_FONT = "NotoColorEmoji"


def tokenize_emojis(text: str) -> List[str]:
    return [glyph for glyph in text]


def uses_fallback_font(codepoint: str) -> bool:
    return ord(codepoint) > 0xFFFF
