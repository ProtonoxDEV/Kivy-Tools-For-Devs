"""Lightweight text engine placeholder with emoji support."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List

EMOJI_REGEX = re.compile(r"[\U0001F300-\U0001FAFF]\ufe0f?")


@dataclass
class TextSegment:
    text: str
    is_emoji: bool = False


class TextEngine:
    def shape(self, text: str) -> List[TextSegment]:
        segments: List[TextSegment] = []
        for part in re.split(f"({EMOJI_REGEX.pattern})", text):
            if not part:
                continue
            segments.append(TextSegment(text=part, is_emoji=bool(EMOJI_REGEX.fullmatch(part))))
        return segments

    def to_canvas_instructions(self, segments: Iterable[TextSegment]) -> list[dict]:
        instructions: list[dict] = []
        for idx, segment in enumerate(segments):
            instructions.append(
                {
                    "text": segment.text,
                    "emoji": segment.is_emoji,
                    "order": idx,
                }
            )
        return instructions
