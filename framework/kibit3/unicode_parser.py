"""Unicode parsing helpers for kibit3."""

from typing import Iterable, List


def grapheme_clusters(text: str) -> List[str]:
    clusters: List[str] = []
    buffer = ""
    for char in text:
        if ord(char) >= 0xDC00 and ord(char) <= 0xDFFF:
            buffer += char
            clusters.append(buffer)
            buffer = ""
        else:
            if buffer:
                clusters.append(buffer)
                buffer = ""
            buffer = char
    if buffer:
        clusters.append(buffer)
    return clusters


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())
