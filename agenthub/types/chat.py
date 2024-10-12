from uuid import UUID
from pydantic import BaseModel

from agenthub.enums.chatmodes import ChatModeEnum
from agenthub.enums.platform import PlatformEnum


class ChatResponse(BaseModel):
    id: UUID
    name: str
    agent_id: int
    organization_id: int
    mode: ChatModeEnum
    platform: PlatformEnum
    responsible: int | None = None
    client_id: UUID | None = None
    created_by_id: int | None = None
    