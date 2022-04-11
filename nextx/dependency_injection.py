from typing import Any, Callable, Dict, Generic, Hashable, Type, TypeVar, Union

T = TypeVar("T")


class Factory(Generic[T]):
    def __init__(self, cls: Type[T]) -> None:
        self.cls = cls

    def __call__(self) -> T:
        return self.cls()


__mappings__: Dict[Union[Type[Any], Hashable], Union[Factory, Type[Any]]] = {}


class Provider:
    def __init__(
        self, interface: Union[Type[Any], Hashable], as_provider: bool = False
    ) -> None:
        self.interface = interface
        self.as_provider = as_provider

    def __call__(self, cls: Type[T]) -> Type[T]:
        if self.as_provider:
            __mappings__[self.interface] = Factory(cls)
        else:
            __mappings__[self.interface] = cls

        return cls
