from typing import Callable, Type

def raises(*exceptions: Type[Exception]):
    def decorator(func: Callable):
        func.__raises__ = exceptions
        return func
    return decorator