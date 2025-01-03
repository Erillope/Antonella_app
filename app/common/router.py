from django.urls import path, URLPattern
from typing import List, Callable

class Router:
    PATHS = {}
    
    @classmethod
    def add_controller_route(cls, controller_route: str) -> None:
        if controller_route not in cls.PATHS:
            cls.PATHS[controller_route] = set()
    
    @classmethod
    def add_route(cls, controller_route: str, route: str, executer: Callable) -> None:
        url = path(controller_route + "/"+ route, executer)
        cls.PATHS[controller_route].add(url)
    
    @classmethod
    def get_routes(cls, controller_route: str) -> List[Callable]:
        return list(cls.PATHS[controller_route])