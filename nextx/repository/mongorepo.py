from typing import Any, Generic, List, Optional, Type, TypeVar
from nextx.domain.models import Entity
from nextx.interfaces.irepository import IRepository
from beanie import Document, PydanticObjectId


TEntity = TypeVar("TEntity", bound=Entity)
DocType = TypeVar("DocType", bound=Document)


class MongoRepository(
    IRepository[TEntity, PydanticObjectId], Generic[TEntity, DocType]
):
    def __init__(
        self,
        model: Type[TEntity],
        schema: Type[DocType],
        session: Optional[Any] = None,
    ):
        self.model = model
        self.schema = schema
        self.session: Optional[Any] = session
        self.seen: List[TEntity] = []

    async def get(self, id: PydanticObjectId) -> Optional[TEntity]:
        document = await self.schema.get(id, session=self.session)
        if document is not None:
            entity = self.model.from_orm(document)
            self.seen.append(entity)
            return entity

    async def delete(self, entity: TEntity) -> bool:
        session = self.session
        await self.schema.find_one(
            self.schema.id == entity.id, session=session
        ).delete_one(session=session)
        return True

    async def list(self, **kwargs) -> List[TEntity]:
        filters = kwargs or {}
        session = self.session
        query = self.schema.find(filters, session=session)
        objects = [self.model.from_orm(record) for record in await query.to_list()]
        self.seen.extend(objects)
        return objects

    async def update(self, entity: TEntity):
        session = self.session
        new_document = self.schema.from_orm(entity)
        await new_document.save(session=session)

    async def add(self, entity: TEntity) -> Optional[TEntity]:
        await self.schema.from_orm(entity).insert(session=self.session)
        self.seen.append(entity)
        return entity

    async def drop(self):
        return await self.schema.delete_all()

    async def count(self, **kwargs) -> int:
        filters = kwargs or {}
        return await self.schema.find(filters).count()

    async def delete_many(self, **kwargs) -> int:
        filters = kwargs or {}
        query = self.schema.find(filters, session=self.session)
        count = await query.count()
        await self.schema.find(filters).delete_many(session=self.session)
        return count
