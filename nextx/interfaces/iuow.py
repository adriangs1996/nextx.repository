from abc import abstractmethod
from typing import Any, Iterable, List, Protocol, Type

from nextx.interfaces.irepository import IRepository


class IUnitOfWork(Protocol):
    repositories: List[IRepository]

    @abstractmethod
    async def __aenter__(self) -> "IUnitOfWork":
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(
        self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Any
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def collect_new_events(self) -> Iterable[Any]:
        raise NotImplementedError
