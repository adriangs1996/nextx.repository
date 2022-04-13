# NEXTX

## Why Nextx

I love FastAPI, but I also love opinionated projects structures. As it turns out, I haven't found a web framework for python that fulfill my needs, so I 
go with the decision of build one of my own.

Of course many "extremely" good frameworks exists for python web development;
we can think of Django, Flask, Pyramid, or the new Kid in 
Town: FastAPI. As a job requirement, I usually find myself
writting Microservices, and usually, in order to build
structured projects, I need to write a LOT of boilerplate
code.

I could use Django and have a batteries included Framework, but that's not good enough though, because
building decoupled components in Django is somewhat cumbersome, it is just not how it works.

I could use Flask, but, I was discourage by globals and
the lack of asynchronous support. In fact, Flask simplicity
is its biggest advantage and biggest flaw. In order to get 
what I want, I would need to install and learn to use a 
bunch of tools.

Here comes FastAPI. FastAPI has all the simpliciy from Flask, but provides more out of the box: 
    
* A big performance boost because the use of starlette
* Autodocumentation with OpenAPI
* Seameless pydantic integration, which I personally love
* Route-based Dependency Injection which makes this framework already superior (in my opinion) to their counterparts

But, when projects grow big, FastAPI needs a lot of infrastructure to work. The thing is, most projects, even
simple ones, require a bunch of configuration and tools in
order to provide abstractions. This is what *Nextx* offers,
cohesion among tools and the facilities and performance of
FastAPI, and, over time, built-in, reusable components that allow developers to make the most out of the framework and their time.  

## Alternatives

This project is highly opinionated about how a project could be developed. It borrows a lot of conventions from
non-pythonic frameworks like Nest.js and .NET Core, but in
my humble opinion, managing these ideas and deploying them
on Python in the best way I can, could significantly improve developer's productivity and likeness to use 
Python as backend framework.

## Stack of patterns

These are fundamentals pattern that should be familiar with in  order to take the most out of the framework

* Repository pattern (needs the concept of drivers)
* Domain Driven Design (represented by Domain Models, Events and Commands. Put domain models as the center of business logic and represented as close as posible to Plain Old Python Classes. Currently, use pydantic models for that. Everything should depend on domain models, and not the way around. Avoid Fat Models)
* Unit Of Work (Provide consistency level over Aggregates transactions)
* Aggregate pattern (Is not implicitly provided, but is promoted)
* Command Handling (Event Driven Design): Builtin support for event handlers, including a RedisMessageSubscriber and the ability to write custom Subscribers and have them integrated with the framework
* Dependency Injection: The whole framework is built around this concept. The goal is never to instantiate an
object by hand, let see if we can achieve that. Right now
uses *Inject* as the Container, maybe we need to
jump to a custom one later on.
* CQRS

## Features

* gRPC support
* IRepository with builtin support for MongoDb, thanks to
*beanie*
* ISubscriber with builtin support for RedisSubscriber and
monolithic subscriber (in process event handling)
* Classic Dependency Injection based on constructor arguments
* Route based Depedency Injection as provided by FastAPI
* Domain Entities with ObjectId as Keys and pydantic support
* Controller Abstraction over FastAPI's Routers
* Custom Exceptions for typical Error's and builtin exception handlers
* Builtin Authorization Services based on simple User entity and JWT

More to come soon

## A taste of Nextx

```python
from nextx.controllers import controller, get
from nextx.dependency_injection import provider
from nextx.server import Server

class IService:
    def get_message(self):
        raise NotImplementedError

@provider(IService)
class Service:
    def __init__(self) -> None:
        self.message = "WTF IT WORKS"

    def get_message(self):
        return self.message


@controller(tags=["My test controller"])
class TestController:
    def __init__(self, service: IService) -> None:
        self.service = service

    @get("/{item_id}")
    async def get_message(self, item_id: str):
        return self.service.get_message()


server = Server()
api = server.build_api("", "testing server")

```