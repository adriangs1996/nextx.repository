from nextx.controllers import controller, get
from nextx.dependency_injection import provider
from nextx.server import Server
from fastapi import Path


class IService:
    def get_message(self):
        raise NotImplementedError


service_count = 0
controller_count = 0


@provider(IService)
class Service:
    def __init__(self) -> None:
        self.message = "WTF IT WORKS"
        global service_count
        service_count += 1

    def get_message(self):
        return self.message


@controller(tags=["My test controller"])
class TestController:
    def __init__(self, service: IService) -> None:
        self.service = service
        global controller_count
        controller_count += 1

    @get("/{item_id}")
    async def get_message(self, item_id: str = Path(...)):
        return f"{self.service.get_message()}, {item_id} controller: {controller_count}, service: {service_count}"


server = Server()
api = server.build_api("", "testing server")
