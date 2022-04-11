from typing import Callable

from fastapi import APIRouter
from fastapi.types import DecoratedCallable


class ApiController(APIRouter):
    """
    Registers endpoints for both a non-trailing-slash and a trailing slash.
    In regards to the exported API schema only the non-trailing slash will be included.

    Examples:

        @router.get("", include_in_schema=False) - not included in the OpenAPI schema,
        responds to both the naked url (no slash) and /

        @router.get("/some/path") - included in the OpenAPI schema as /some/path,
        responds to both /some/path and /some/path/

        @router.get("/some/path/") - included in the OpenAPI schema as /some/path,
        responds to both /some/path and /some/path/

    Co-opted from https://github.com/tiangolo/fastapi/issues/2060#issuecomment-974527690
    """

    def api_route(self, path: str, *, include_in_schema: bool = True, **kwargs) -> Callable[[DecoratedCallable], DecoratedCallable]:
        given_path = path
        path_no_slash = given_path[:-1] if given_path.endswith("/") else given_path

        add_nontrailing_slash_path = super().api_route(
            path_no_slash,
            include_in_schema=include_in_schema,
            **kwargs
        )

        add_trailing_slash_path = super().api_route(
            path_no_slash + "/",
            include_in_schema=False,
            **kwargs
        )

        def add_path_and_trailing_slash(func: DecoratedCallable) -> DecoratedCallable:
            add_trailing_slash_path(func)
            return add_nontrailing_slash_path(func)

        return add_trailing_slash_path if given_path == "/" else add_path_and_trailing_slash
