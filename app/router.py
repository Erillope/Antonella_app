from .controller import Controller
from django.urls import path
from typing import List

class Router:
    def __init__(self) -> None:
        self.controllers : List[Controller] = []
    
    def add(self, controller: Controller) -> None:
        self.controllers.append(controller)
    
    def get_routes(self) -> List:
        urls = []
        for controller in self.controllers:
            for name, view in controller.generate_views():
                url = path(f"{controller.route_prefix}/{name}", view)
                urls.append(url)
        return urls