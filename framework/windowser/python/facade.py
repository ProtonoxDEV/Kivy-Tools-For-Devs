"""Lightweight facade for bridging Kivy apps to the Windowser native layer.

This module avoids heavy dependencies so it can be vendored directly into
python-for-android projects. Hook the methods to Pyjnius-provided Java
classes defined in the `android` folder.
"""

from __future__ import annotations

import logging
from typing import Callable, Optional

logger = logging.getLogger("protonox.windowser")


class PermissionManager:
    def __init__(self, requester: Callable[[list[str]], bool]):
        self.requester = requester

    def ensure(self, permissions: list[str]) -> bool:
        logger.debug("Requesting permissions: %s", permissions)
        try:
            return bool(self.requester(permissions))
        except Exception as exc:  # noqa: BLE001
            logger.exception("Permission request failed: %%s", exc)
            return False


class NotificationCenter:
    def __init__(self, dispatcher: Callable[[str, str], None]):
        self.dispatcher = dispatcher

    def notify(self, title: str, message: str) -> None:
        logger.debug("Dispatching notification: %s - %s", title, message)
        try:
            self.dispatcher(title, message)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Notification dispatch failed: %%s", exc)


class StorageBridge:
    def __init__(self, saver: Callable[[str, bytes], bool], loader: Callable[[str], bytes]):
        self.saver = saver
        self.loader = loader

    def save(self, path: str, data: bytes) -> bool:
        logger.debug("Saving blob to %s (%d bytes)", path, len(data))
        try:
            return bool(self.saver(path, data))
        except Exception as exc:  # noqa: BLE001
            logger.exception("Storage save failed: %%s", exc)
            return False

    def load(self, path: str) -> Optional[bytes]:
        logger.debug("Loading blob from %s", path)
        try:
            return self.loader(path)
        except FileNotFoundError:
            logger.warning("Storage path not found: %s", path)
            return None
        except Exception as exc:  # noqa: BLE001
            logger.exception("Storage load failed: %%s", exc)
            return None


class BackgroundService:
    def __init__(self, starter: Callable[[str], None], stopper: Callable[[str], None]):
        self.starter = starter
        self.stopper = stopper

    def start(self, name: str) -> None:
        logger.info("Starting background service: %s", name)
        try:
            self.starter(name)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Start service failed: %%s", exc)

    def stop(self, name: str) -> None:
        logger.info("Stopping background service: %s", name)
        try:
            self.stopper(name)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Stop service failed: %%s", exc)
