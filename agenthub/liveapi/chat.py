from typing import Any, Awaitable, Callable, Unpack
from uuid import UUID
from agenthub.liveapi.connection import Connection
from agenthub.types.message import Message
from agenthub.types.message_dict import MessageDict
from agenthub.types.message_response import MessageResponse


class ChatAPI:
    def __init__(
        self,
        connection: Connection,
        chat_id: UUID
    ) -> None:
        self.connection = connection
        self.chat_id = chat_id

    async def send_message(
        self,
        **data: Unpack[MessageDict]
    ):
        message = Message(**data, chat_id=self.chat_id)

        await self.connection.send_message(message)
    
    async def receive_message(
        self,
        handler: Callable[[MessageResponse], Awaitable[Any] | Any]
    ):
        await self.connection.receive_message(handler)