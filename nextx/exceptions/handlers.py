from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from nextx.domain.viewmodels import DataResponse
from nextx.exceptions.definitions import (
    NotFoundError,
    ForbiddenError,
    InternalServerError,
    InvalidRequestError,
)


async def not_found_exception_handler(request: Request, exc: NotFoundError):
    data = DataResponse(
        message=f"Resource named: {exc.name} not found!",
        status_code=status.HTTP_404_NOT_FOUND,
    )

    return JSONResponse(status_code=status.HTTP_200_OK, content=data.dict())


async def forbidden_exception_handler(request: Request, exc: ForbiddenError):
    data = DataResponse(
        message=f"Access Forbidden!",
        status_code=status.HTTP_401_UNAUTHORIZED,
        data=exc.details,
    )

    return JSONResponse(status_code=status.HTTP_200_OK, content=data.dict())


async def internal_server_exception_handler(request: Request, exc: InternalServerError):
    data = DataResponse(
        message=f"Server failed unexpectedly",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        data=exc.details,
    )

    return JSONResponse(status_code=status.HTTP_200_OK, content=data.dict())


async def invalid_request_exception_handler(request: Request, exc: InvalidRequestError):
    data = DataResponse(
        message=f"Bad Request",
        status_code=status.HTTP_400_BAD_REQUEST,
        data=exc.details,
    )

    return JSONResponse(status_code=status.HTTP_200_OK, content=data.dict())
