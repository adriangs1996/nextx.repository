import abc
from typing import List, Optional, Type, TypeVar
from nextx.domain.models import Entity
from nextx.interfaces.iremotes import IPublicationProjectRemoteClient
from grpclib.client import Channel
from .protos.blueprint_grpc import BlueprintServiceStub
from .protos.blueprint_pb2 import (
    BusinessUnitActiveBlueprintRequest,
    BusinessUnitBlueprintsRequest,
)

BusinessUnitModel = TypeVar("BusinessUnitModel", bound=Entity)
BlueprintModel = TypeVar("BlueprintModel", bound=Entity)


class PublicationProjectGrpcAsyncClient(
    IPublicationProjectRemoteClient[BusinessUnitModel, BlueprintModel], abc.ABC
):
    def __init__(self, url: str, blueprint_model: Type[BlueprintModel]) -> None:
        self.blueprint_model = blueprint_model
        channel = Channel(url)
        self.service = BlueprintServiceStub(channel)

    async def get_business_unit_active_project_async(
        self, business_unit: BusinessUnitModel
    ) -> Optional[BlueprintModel]:
        request = BusinessUnitActiveBlueprintRequest(id=str(business_unit.id))

        response = await self.service.GetActiveProjectForBU(request)

        if response.active_project is not None:
            return self.blueprint_model.from_orm(response.active_project)

        return None

    async def get_all_business_unit_projects_async(
        self, business_unit: BusinessUnitModel
    ) -> List[BlueprintModel]:
        request = BusinessUnitBlueprintsRequest(id=str(business_unit.id))

        response = await self.service.GetBusinessUnitActiveProjects(request)

        return list(
            self.blueprint_model.from_orm(blueprint) for blueprint in response.projects
        )

    def get_all_business_unit_projects(self, business_unit):
        raise NotImplementedError

    def get_business_unit_active_project(self, business_unit):
        raise NotImplementedError
