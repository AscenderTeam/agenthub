from typing import Literal
from uuid import UUID
from pydantic import BaseModel

from agenthub.enums.datatype import DataTypeEnum
from agenthub.enums.emergency import EmergencyTypeEnum
from agenthub.enums.messagetype import MessageTypeEnum


class MessageResponse(BaseModel):
    id: int
    content: str | dict | None  # Some file(image,audio,video) url or text

    data_type: DataTypeEnum
    message_type: MessageTypeEnum

    text_representation: str | None = None
    emotional_indicator: dict[str, float] | None = None
    reply_to_message_id: int | None = None

    agent_id: int | None = None
    user_id: int | None = None
    client_id: UUID | None = None

    chat_id: UUID

    tool_called_id: int | None = None
    tool_status: Literal['started', 'finished', 'error'] | None = None
    tool_started_input: str | None = None
    tool_finished_output: str | None = None
    tool_error_detail: str | None = None

    specialist_required: EmergencyTypeEnum | None = None