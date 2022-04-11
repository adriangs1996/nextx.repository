from typing import List, Optional

from decouple import config  # type: ignore
from fastapi import Query, Header, Depends
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, JWTError
from nextx.domain.models import LoggedInUser
from nextx.exceptions.definitions import ForbiddenError


def get_filters(filters: Optional[str] = Query(None)) -> dict:
    if filters is None:
        return {}

    try:
        result: dict = {}
        # filters are separeted by |
        filters_list = filters.split("|")
        for f in filters_list:
            # key and value are separated by :
            key, value = f.split(":")
            if "," in value:
                result[key] = value.split(",")
            else:
                result[key] = value
        return result
    except Exception as e:
        return {}


def get_authorization_header(authorization: str = Header(None, alias="Authorization")):
    scheme, param = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != "bearer":
        raise ForbiddenError(
            name="Not authenticated Error",
            details={
                "headers": {"WWW-Authenticate": "Bearer"},
                "error_source": "No Bearer token supplied or invalid scheme",
            },
        )

    return param


def auth_user(token: str = Depends(get_authorization_header)) -> LoggedInUser:
    try:
        # Check if this token was sign by our authorization server
        payload = jwt.decode(
            token, config("SECRET_JWT_KEY"), algorithms=[jwt.ALGORITHMS.HS256]
        )
        # username must come as subject
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise ForbiddenError(
                name="Invalid access token",
                details={
                    "headers": {"WWW-Authenticate": "Bearer"},
                    "error_source": "Supplied token does not contains username",
                },
            )
        token_scopes = payload.get("scopes", [])
        token_roles = payload.get("roles", [])
    except JWTError as e:
        raise ForbiddenError(
            name="Invalid access token",
            details={
                "headers": {"WWW-Authenticate": "Bearer"},
                "error_source": "Supplied token contains errors",
                "error": str(e),
            },
        )
    return LoggedInUser(token=token, scopes=token_scopes, roles=token_roles)


class AuthorizeService:
    """
    Implements the basic authentication logic for services that conforms
    this microservice. This is meant to be subclassed by a concrete
    Service class.
    """

    def __init__(
        self, scopes: Optional[List[str]] = None, roles: Optional[List[str]] = None
    ):
        self._scopes = scopes
        self._roles = roles

    def __call__(self, user: LoggedInUser = Depends(auth_user)) -> LoggedInUser:
        if self._roles and not any(role in self._roles for role in user.roles):
            raise ForbiddenError(
                name="Invalid user Role for this action",
                details={
                    "headers": {"WWW-Authenticate": f"Bearer roles={self._roles}"},
                    "error_source": "Invalid user Role for this action",
                },
            )
        if not self._scopes or all(scope in user.scopes for scope in self._scopes):
            return user

        raise ForbiddenError(
            name="Invalid user",
            details={
                "headers": {"WWW-Authenticate": f"Bearer scopes={self._scopes}"},
                "error_source": "User has no permission to access this resource",
            },
        )
