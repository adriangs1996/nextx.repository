from abc import abstractmethod
from typing import List, Optional, Protocol, TypeVar
from nextx.domain.models import Entity

TBU = TypeVar("TBU", bound=Entity)
TBlueprint = TypeVar("TBlueprint", bound=Entity)


class IPublicationProjectRemoteClient(Protocol[TBU, TBlueprint]):
    @abstractmethod
    def get_business_unit_active_project(
        self, business_unit: TBU
    ) -> Optional[TBlueprint]:
        raise NotImplementedError

    @abstractmethod
    async def get_business_unit_active_project_async(
        self, business_unit: TBU
    ) -> Optional[TBlueprint]:
        raise NotImplementedError

    @abstractmethod
    def get_all_business_unit_projects(self, business_unit: TBU) -> List[TBlueprint]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_business_unit_projects_async(
        self, business_unit: TBU
    ) -> List[TBlueprint]:
        raise NotImplementedError
