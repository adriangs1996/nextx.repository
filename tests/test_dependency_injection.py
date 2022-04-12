from nextx.dependency_injection import Factory, provider, service, __mappings__
import inject


def configure_injector():
    def binders(binder: inject.Binder):
        for k, v in __mappings__.items():
            if isinstance(v, Factory):
                binder.bind_to_provider(k, v)
            else:
                binder.bind(k, v())

    inject.clear_and_configure(binders)


def test_provider_injects_params():
    class Interface:
        def message(self):
            raise NotImplementedError

    @provider(Interface)
    class A:
        def __init__(self) -> None:
            self._message = "Hello"

        def message(self):
            return self._message

    @service
    class B:
        def __init__(self, a: Interface) -> None:
            self.a = a

        def call(self):
            return self.a.message()

    configure_injector()
    b = B()  # type: ignore
    assert b.call() == "Hello"
    __mappings__ = {}


def test_provider_works_on_functions():
    class Interface:
        def message(self):
            raise NotImplementedError

    class A:
        def __init__(self) -> None:
            self._message = "Hello"

        def message(self):
            return self._message

    @provider(Interface)
    def get_a_instance():
        return A()

    @service
    class B:
        def __init__(self, a: Interface) -> None:
            self.a = a

        def call(self):
            return self.a.message()

    configure_injector()
    b = B()  # type: ignore
    assert b.call() == "Hello"
    __mappings__ = {}


def test_service_works_on_functions():
    pass
