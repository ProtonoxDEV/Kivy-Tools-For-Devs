"""Remote console stub."""

from dataclasses import dataclass


@dataclass
class ConsoleMessage:
    level: str
    text: str


def format_message(msg: ConsoleMessage) -> str:
    return f"[{msg.level.upper()}] {msg.text}"
