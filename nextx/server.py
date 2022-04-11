import abc
from typing import Callable, List
import logging
import uvicorn
import inject
from nextx.controllers import ApiController
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
        inject_configurator: Callable[[inject.Binder], None],
        controllers: List[ApiController],
    ) -> None:
        self.inject_configurator = inject_configurator
        self.controllers = controllers

    def _setup(self):
        _config_logger()
        inject.configure_once(self.inject_configurator, False)

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

        return api
