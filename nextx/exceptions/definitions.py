from typing import Optional


class NotFoundError(Exception):
    def __init__(self, name: str):
        self.name = name


class ForbiddenError(Exception):
    def __init__(self, name: str, details: Optional[dict] = None):
        self.name = name
        self.details = details


class InvalidRequestError(Exception):
    def __init__(self, details: Optional[dict]):
        self.details = details


class InternalServerError(Exception):
    def __init__(self, details: Optional[dict]):
        self.details = details
