"""Notification helpers for Protonox."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class NotificationChannel:
    id: str
    name: str
    importance: str = "default"


def build_notification_payload(title: str, message: str, channel: NotificationChannel) -> Dict[str, str]:
    return {
        "title": title,
        "message": message,
        "channel_id": channel.id,
        "channel_name": channel.name,
        "importance": channel.importance,
    }
