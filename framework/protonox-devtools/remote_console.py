from __future__ import annotations

import logging
import socket
import threading

logger = logging.getLogger("protonox.remote_console")


class RemoteConsole:
    def __init__(self, host: str = "0.0.0.0", port: int = 8023):
        self.host = host
        self.port = port
        self._server: socket.socket | None = None

    def start(self) -> None:
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((self.host, self.port))
        self._server.listen(1)
        logger.info("Remote console listening on %s:%s", self.host, self.port)
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def _accept_loop(self) -> None:
        assert self._server is not None
        while True:
            conn, addr = self._server.accept()
            logger.info("Console connected: %s", addr)
            threading.Thread(target=self._handle_client, args=(conn,), daemon=True).start()

    def _handle_client(self, conn: socket.socket) -> None:
        with conn:
            conn.sendall(b"Protonox console ready\n>>> ")
            buffer = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                buffer += chunk
                if b"\n" in buffer:
                    line, buffer = buffer.split(b"\n", 1)
                    self._execute(line.decode().strip(), conn)
                    conn.sendall(b"\n>>> ")

    def _execute(self, command: str, conn: socket.socket) -> None:
        try:
            result = eval(command, {})  # noqa: S307 - trusted dev environment
            conn.sendall(str(result).encode())
        except Exception as exc:  # noqa: BLE001
            conn.sendall(f"ERR: {exc}".encode())
