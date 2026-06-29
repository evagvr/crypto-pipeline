import asyncio
import websockets
import json
import logging
from typing import Callable

logger = logging.getLogger(__name__)


class BinanceWebsocketClient:
    def __init__(self, symbols: list, on_message: Callable):
        self.url = "wss://stream.binance.com:9443/ws/"
        self.url += "/".join(s + "@trade" for s in symbols)
        self.on_message = on_message
        self._running = False

    async def connect(self):
        self._running = True
        try:
            async with websockets.connect(self.url) as websocket:
                while self._running:
                    message = await websocket.recv()
                    message = json.loads(message)
                    self.on_message(message)
        except websockets.exceptions.ConnectionClosed:
            logger.warning("Websocket connection closed")
        except Exception as e:
            logger.error(e)

    def disconnect(self):
        self._running = False
        logger.info("Websocket is disconnected")
