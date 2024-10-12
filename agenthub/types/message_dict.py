from typing import NotRequired, TypedDict
from uuid import UUID

from agenthub.enums.datatype import DataTypeEnum


class MessageDict(TypedDict):
    content: str | dict | None  # Some file(image,audio,video) url or text
    data_type: DataTypeEnum

    reply_to_message_id: NotRequired[int | None]
    client_id: NotRequired[UUID | None]