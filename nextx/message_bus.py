from functools import singledispatchmethod
import logging
from typing import Any, List, Optional, Union
from nextx.interfaces.iuow import IUnitOfWork
import inject
from fastapi import BackgroundTasks
from nextx.domain.events import Event
from nextx.domain.commands import Command
from decouple import config
import aioredis as redis

Message = Union[Event, Command]
logger = logging.getLogger("logger")


class RedisMessageBus:
    def __init__(self, background_tasks: Optional[BackgroundTasks] = None) -> None:
        self.background_tasks = background_tasks
        self.uow: IUnitOfWork = inject.instance(IUnitOfWork)

    async def handle(self, message: Message):
        queue = [message]
        while queue:
            message = queue.pop(0)
            if isinstance(message, Event):
                await self._send_event(message, queue)
            else:
                await self._send_command(message, queue)

    async def _send_event(self, event: Event, queue: List[Message]):
        try:
            logger.info("Handling event %s", event)
            await self._handle_event(event)
            queue.extend(self.uow.collect_new_events())
        except Exception:
            logger.exception("Exception handling event %s", event)

    async def _send_command(self, cmd: Command, queue: List[Message]):
        logger.info("Handling command %s", cmd)
        try:
            await self._handle_command(cmd)
            queue.extend(self.uow.collect_new_events())
        except Exception:
            logger.exception("Exception handling command %s", cmd)
            raise

    # =======================================    EVENT  HANDLING   ================================ #

    async def _send_event_to_outside(self, channel: str, event: Event):
        host: Any = config("REDIS_HOST")
        assert isinstance(host, str)
        client: redis.Redis = await redis.from_url(f"redis://{host}")
        await client.publish(channel, event.json())

    async def _submit(self, etype: str, event: Event):
        if self.background_tasks is not None:
            self.background_tasks.add_task(self._send_event_to_outside, etype, event)
        else:
            await self._send_event_to_outside(etype, event)

    @singledispatchmethod
    async def _handle_event(self, event: Event):
        pass

    @singledispatchmethod
    async def _handle_command(self, cmd: Command):
        pass
