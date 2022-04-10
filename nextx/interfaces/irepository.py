from abc import abstractmethod
from typing import Any, List, Mapping, Optional, Protocol, TypeVar

TEntity = TypeVar("TEntity")
TId = TypeVar("TId", contravariant=True)


class IRepository(Protocol[TEntity, TId]):
    seen: List[TEntity]

    @abstractmethod
    async def add(self, entity: TEntity) -> Optional[TEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, id: TId) -> Optional[TEntity]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entity: TEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def list(self, **kwargs: Mapping[str, Any]) -> List[TEntity]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: TEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def drop(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def count(self, filters: Optional[Mapping[str, Any]] = None) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete_many(self, filters: Optional[Mapping[str, Any]] = None) -> int:
        raise NotImplementedError
