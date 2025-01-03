from .router import Router
from .create_view import create_post, create_put, create_delete, create_get
from functools import wraps
from .responses import invalid_field_response
from rest_framework.serializers import Serializer
from typing import Type

class Executer:
    def __init__(self, executer, _class, required_request=True):
        self.executer = executer
        self._class = _class
        self.required_request = required_request
        
    def do(self, request=None, **kwargs):
        if self.required_request:
            return self.executer(self._class, request)
        else:
            return self.executer(self._class, **kwargs)
    
class ControllerMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        for attr_name, attr_value in dct.items():
            if hasattr(attr_value, "_route_values"):
                values = attr_value._route_values.copy()
                name = values['name']
                if values['method'] == 'POST' or values['method'] == 'PUT':
                    input_serializer = values['input_serializer']
                    executer = Executer(values['executer'], new_class)
                    view = create_post(input_serializer, executer , name)
                if values['method'] == 'PUT':
                    input_serializer = values['input_serializer']
                    executer = Executer(values['executer'], new_class)
                    view = create_put(input_serializer, executer , name)
                if values['method'] == 'DELETE':
                    executer = Executer(values['executer'], new_class, required_request=False)
                    view = create_delete(executer, name)
                if values['method'] == 'GET':
                    executer = Executer(values['executer'], new_class, required_request=False)
                    view = create_get(executer, name)
                Router.add_controller_route(new_class.controller_route)
                Router.add_route(new_class.controller_route, values['route'], view)
        return new_class
    
class Controller(metaclass=ControllerMeta):
    @classmethod
    def post(cls, route: str, name: str, input_serializer: Type[Serializer]):
        def decorador(metodo):
            @wraps(metodo)
            def wrapper(cls, request, *args, **kwargs):
                serializer = input_serializer(data=request.data)
                if not serializer.is_valid(): return invalid_field_response(serializer.errors)
                return metodo(cls, serializer)
            wrapper._route_values = {'route': route, 'executer': wrapper,
                                     'input_serializer': input_serializer, 'name': name,'method': 'POST'}
            return wrapper
        return decorador
    
    @classmethod
    def put(cls, route: str, name: str, input_serializer: Type[Serializer]):
        def decorador(metodo):
            @wraps(metodo)
            def wrapper(cls, request, *args, **kwargs):
                serializer = input_serializer(data=request.data)
                if not serializer.is_valid(): return invalid_field_response(serializer.errors)
                return metodo(cls, serializer)
            wrapper._route_values = {'route': route, 'executer': wrapper,
                                     'input_serializer': input_serializer, 'name': name, 'method': 'PUT'}
            return wrapper
        return decorador
    
    @classmethod
    def delete(cls, route: str, name: str):
        def decorador(metodo):
            @wraps(metodo)
            def wrapper(cls, *args, **kwargs):
                return metodo(cls, **kwargs)
            wrapper._route_values = {'route': route, 'executer': wrapper,'name': name, 'method': 'DELETE'}
            return wrapper
        return decorador
    
    @classmethod
    def get(cls, route: str, name: str):
        def decorador(metodo):
            @wraps(metodo)
            def wrapper(cls, *args, **kwargs):
                return metodo(cls, **kwargs)
            wrapper._route_values = {'route': route, 'executer': wrapper,'name': name, 'method': 'GET'}
            return wrapper
        return decorador