from uuid import UUID
from pydantic import BaseModel

from agenthub.enums.datatype import DataTypeEnum


class Message(BaseModel):
    content: str | dict | None  # Some file(image,audio,video) url or text
    data_type: DataTypeEnum

    reply_to_message_id: int | None = None
    client_id: UUID | None = None

    chat_id: UUID