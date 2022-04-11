from typing import List
from nextx.pubsub.isusbscriber import ISubscriber
import aioredis as redis
from decouple import config
import async_timeout
import asyncio
import logging
import json
import abc


logger = logging.getLogger("logger")


class RedisSubscriber(ISubscriber, abc.ABC):
    def __init__(self):
        self.client = redis.Redis(host=config("REDIS_HOST"), decode_responses=True)
        self.pub_sub = self.client.pubsub()

    async def init_subscriber(self, events: List[str]):
        await self._subscribe_to_event(events)

    async def _subscribe_to_event(self, event: str | List[str]):
        if isinstance(event, list):
            await self.pub_sub.subscribe(*event)
        else:
            await self.pub_sub.subscribe(event)

    async def loop(self):
        while True:
            try:
                async with async_timeout.timeout(1):
                    event, data = await self.get_message()
                    if event is not None and data is not None:
                        await self.handle_message(event, data)
                    await asyncio.sleep(0.01)
            except asyncio.TimeoutError:
                pass

    async def get_message(self):
        message = await self.pub_sub.get_message(ignore_subscribe_messages=True)
        if message is not None:
            event: str = message["channel"]
            logger.info(f"Received message: {event}")
            data: dict = json.loads(message["data"])
            return event, data
        return None, None

    @abc.abstractmethod
    async def handle_message(self, event_type: str, event_data: dict):
        raise NotImplementedError
