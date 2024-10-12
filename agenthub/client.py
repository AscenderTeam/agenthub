from typing import List, Literal
from uuid import UUID
from aiohttp import ClientSession

from agenthub.debugger import AgentDebugger
from agenthub.enums.platform import PlatformEnum
from agenthub.types.chat import ChatResponse


class Client:
    def __init__(
            self,
            api_key: str,
            platform: PlatformEnum = PlatformEnum.UNKNOWN,
            url: str = "https://api.ascender-ai.com",
            mode: Literal["development", "production"] = "production",
            api_version: Literal["v1"] = "v1",
            **aiohttp_configs
        ) -> None:
        self.api_key = api_key
        self.url = url
        self.mode = mode
        self.api_version = api_version
        
        self.session_client = ClientSession(self.url,
                                            headers={
                                                "Authorization": f"Bearer {self.api_key}"
                                            },
                                            **aiohttp_configs)
    
    @property
    def debugger(self) -> AgentDebugger:
        return AgentDebugger(self.session_client)
    
    async def get_chats(self, customer_id: UUID) -> List[ChatResponse]:
        pass

    async def get_chat(self, chat_id: UUID) -> ChatResponse | None:
        pass
    
    async def select_chat(self, chat_id: UUID) -> ChatResponse:
        if not (chat := await self.get_chat(chat_id)):
            raise

        