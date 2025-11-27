from __future__ import annotations

import asyncio
import logging
import websockets

logger = logging.getLogger("protonox.ws_debugger")


async def debug_server(host: str = "0.0.0.0", port: int = 8765) -> None:
    async def handler(websocket):  # type: ignore[no-untyped-def]
        logger.info("Debugger client connected")
        async for message in websocket:
            logger.debug("Received: %s", message)
            await websocket.send(f"echo: {message}")

    async with websockets.serve(handler, host, port):
        logger.info("WebSocket debugger listening on %s:%s", host, port)
        await asyncio.Future()
