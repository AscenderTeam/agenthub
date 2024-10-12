from aiohttp import ClientSession


class AgentDebugger:
    def __init__(self,
                 client: ClientSession) -> None:
        self.client = client
    
    async def get_api_info(self):
        pass