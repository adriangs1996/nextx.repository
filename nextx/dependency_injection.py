from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Hashable,
    Optional,
    Type,
    TypeVar,
    Union,
)
from inject import autoparams

T = TypeVar("T")


class Factory(Generic[T]):
    def __init__(self, cls: Union[Type[T], Callable]) -> None:
        self.cls = cls

    def __call__(self) -> Union[T, Any]:
        return self.cls()


__mappings__: Dict[Union[Type[Any], Hashable], Union[Factory, Type[Any], Callable]] = {}


def service(fn: Union[Type[T], Callable[..., Any]]) -> Union[Type[T], Callable]:
    wrapper = autoparams()
    fn = wrapper(fn)
    return fn


def provider(
    interface: Optional[Union[Type[Any], Hashable]] = None,
    as_provider: bool = True,
) -> Callable[[Union[Type[T], Callable]], Type[T]]:
    def decorator(cls: Union[Type[T], Callable[..., Any]]) -> Union[Type[T], Callable]:
        if interface is None:
            key = cls
        else:
            key = interface

        if as_provider:
            __mappings__[key] = Factory(cls)
        else:
            __mappings__[key] = cls

        return cls

    return decorator
