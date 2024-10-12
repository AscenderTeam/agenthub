from asyncio import iscoroutine
from typing import Awaitable, Callable, Literal, overload
from uuid import UUID
from socketio.async_client import AsyncClient

from agenthub.types.message import Message


class Connection:
    def __init__(
        self,
        url: str,
        apikey: str,
        mode: Literal["development", "production"]
    ) -> None:
        self.url = url
        # TODO: Add functionality to configurate AsyncClient
        self.connection = AsyncClient()
        self.apikey = apikey

    async def connect(self):
        await self.connection.connect(
            url=self.url,
            headers={
                "Session-Token": self.apikey
            },
            socketio_path="/api/ws/socket.io"
        )

    async def disconnect(self):
        await self.connection.disconnect()

    async def send_message(self, content: Message):
        _jsonified = content.model_dump_json()

        await self.connection.emit(
            "chat-message",
            data=_jsonified,
            namespace="/cmessages"
        )
    
    async def receive_message(self, callback: Callable[[Message], Awaitable[None] | None]):
        await self.connection.on("message", callback, "/cmessages")