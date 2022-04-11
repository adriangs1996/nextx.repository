from abc import abstractmethod
from typing import Any, Protocol


class ISubscriber(Protocol):
    @abstractmethod
    async def init_subscriber(self):
        raise NotImplementedError

    @abstractmethod
    async def loop(self):
        raise NotImplementedError

    @abstractmethod
    async def get_message(self):
        raise NotImplementedError

    @abstractmethod
    async def handle_message(self, event: str, event_data: Any):
        raise NotImplementedError
        
