import asyncio
from typing import Callable, List, Optional
import logging
import uvicorn
import inject
from nextx.controllers import ApiController
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nextx.dependency_injection import Factory
from nextx.exceptions.definitions import (
    ForbiddenError,
    InternalServerError,
    InvalidRequestError,
    NotFoundError,
)
from nextx.exceptions.handlers import (
    forbidden_exception_handler,
    not_found_exception_handler,
    internal_server_exception_handler,
    invalid_request_exception_handler,
)
from asyncio import Task
import grpclib.server
from grpclib.utils import graceful_exit
from nextx.pubsub.isusbscriber import ISubscriber


def _config_logger():
    FORMAT: str = "%(levelprefix)s %(asctime)s | %(message)s"
    # create logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = uvicorn.logging.DefaultFormatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")  # type: ignore

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


class Server:
    def __init__(
        self,
        controllers: List[ApiController],
        inject_configurator: Optional[Callable[[inject.Binder], None]],
        events: Callable[[], List[str]] = lambda: [],
    ) -> None:
        self.inject_configurator = inject_configurator
        self.controllers = controllers
        self.grpc_server: Optional[Task] = None
        self.subscriber: Optional[Task] = None
        self.events = events()

    def _setup(self):
        _config_logger()
        from nextx.dependency_injection import __mappings__

        def config(binder: inject.Binder):
            for dependency, factory in __mappings__.items():
                if isinstance(factory, Factory):
                    binder.bind_to_provider(dependency, factory)
                else:
                    binder.bind(dependency, factory)

            if self.inject_configurator is not None:
                self.inject_configurator(binder)

        inject.configure_once(config, False)

    async def _setup_grpc_server(self, grpc_service):
        server = grpclib.server.Server([grpc_service])  # type: ignore

        with graceful_exit([server]):
            await server.start()
            logger = logging.getLogger("logger")
            logger.info(f"Serving gRPC on port 50051")
            await server.wait_closed()

    async def _setup_subscriber(self, subscriber: ISubscriber):
        await subscriber.init_subscriber(self.events)
        await subscriber.loop()

    def shutdown(self):
        if self.grpc_server is not None:
            self.grpc_server.cancel()

        if self.subscriber is not None:
            self.subscriber.cancel()

    def build_api(self, server_prefix: str, title: str, version="0.1.0") -> FastAPI:
        self._setup()

        api = FastAPI(
            docs_url=None,
            redoc_url=f"{server_prefix}/docs",
            openapi_url=f"{server_prefix}/openapi.json",
            title=title,
            version=version,
            contact={"name": "NextX Team"},
        )

        origins = ["*"]

        api.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        for controller in self.controllers:
            api.include_router(controller, prefix=server_prefix)

        api.add_exception_handler(NotFoundError, not_found_exception_handler)
        api.add_exception_handler(
            InternalServerError, internal_server_exception_handler
        )
        api.add_exception_handler(ForbiddenError, forbidden_exception_handler)
        api.add_exception_handler(
            InvalidRequestError, invalid_request_exception_handler
        )

        try:
            grpc_service = inject.instance("grpc_service")
        except inject.InjectorException:
            grpc_service = None

        if grpc_service is not None:
            self.grpc_server = asyncio.create_task(
                self._setup_grpc_server(grpc_service)
            )

        try:
            subscriber = inject.instance(ISubscriber)
        except inject.InjectorException:
            subscriber = None

        if subscriber is not None:
            self.subscriber = asyncio.create_task(self._setup_subscriber(subscriber))

        return api
