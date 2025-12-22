# -*- coding: utf-8 -*-
"""
@Author: Eric Santos <ericshantos13@gmail.com>
Launcher module for the fake news prediction server.
"""

import json
import logging
import asyncio
import websockets
from ..core import NewsClassifier

logger = logging.getLogger(__name__)


class Launcher:
    """
    WebSocket server launcher for handling prediction requests.

    This class encapsulates the logic required to:
        - Accept WebSocket connections
        - Receive text-based messages
        - Perform asynchronous predictions using a trained model
        - Send structured JSON responses back to clients

    The prediction itself is executed in a separate thread in order to
    avoid blocking the asyncio event loop.
    """

    def __init__(self, classifier: NewsClassifier) -> None:
        """
        Initialize the Launcher with a trained classifier.

        Args:
            classifier (NewsClassifier):
                An instance of a trained news classification model
                responsible for performing predictions.
        """
        self.classifier = classifier

    async def handler(
        self,
        websocket: websockets.WebSocketServerProtocol
    ) -> None:
        """
        Handle a WebSocket client connection.

        This coroutine is invoked for each new client connection.
        It listens for incoming messages, validates them, triggers
        predictions, and sends back JSON-formatted responses.

        Args:
            websocket (websockets.WebSocketServerProtocol):
                The active WebSocket connection with the client.

        Raises:
            websockets.ConnectionClosed:
                Raised when the client closes the connection.
        """
        logger.info("[CONNECTION ESTABLISHED]")

        try:
            async for message in websocket:
                logger.debug(f"[RECEIVED MESSAGE] {message}")

                if not isinstance(message, str) or not message.strip():
                    logger.warning("[INVALID MESSAGE TYPE]")

                    await websocket.send(json.dumps({
                        "ok": False,
                        "message": "Invalid message. Please send a non-empty string."
                    }))
                    continue

                try:
                    prediction = await asyncio.to_thread(
                        self.classifier.predict,
                        message
                    )

                    response = json.dumps({
                        "ok": True,
                        "prediction": prediction
                    })

                except Exception as exc:
                    logger.exception(f"[PREDICTION ERROR] {exc}")

                    response = json.dumps({
                        "ok": False,
                        "message": "An error occurred during prediction."
                    })

                await websocket.send(response)
                logger.debug(f"[SENT RESPONSE] {response}")

        except websockets.ConnectionClosed:
            logger.info("[CONNECTION CLOSED]")

        except Exception as exc:
            logger.exception(f"[HANDLER ERROR] {exc}")

    async def run(self, host: str, port: int) -> None:
        """
        Start the WebSocket server and keep it running indefinitely.

        This method binds the server to the specified host and port
        and blocks execution until the task is cancelled.

        Args:
            host (str):
                Host address where the server will listen (e.g., "localhost").
            port (int):
                TCP port number for the WebSocket server.

        Raises:
            asyncio.CancelledError:
                Raised when the server task is cancelled during shutdown.
        """
        logger.info(f"[SERVER RUNNING] on ws://{host}:{port}")

        async with websockets.serve(self.handler, host, port):
            try:
                await asyncio.Event().wait()
            except asyncio.CancelledError:
                logger.info("[SERVER SHUTTING DOWN]")
