from typing import Type, Callable
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from app.responses import success_response
from app.validate import validate
from app.serializer_mapper import SerializerMapper
from enum import Enum

class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    
class ViewCreator:
    def __init__(self, path: str,executer: Callable,
                 name: str, http_method: HttpMethod, mapper: SerializerMapper, serializer_class: Type[Serializer] = None) -> None:
        self.path = path
        self.serializer_class = serializer_class
        self.executer = executer
        self.name = name
        self.http_method = http_method
        self.mapper = mapper
        
    def create(self) -> Callable:
        if self.http_method == HttpMethod.POST:
            return create_post(self.serializer_class, self.executer, self.name, self.mapper)
        elif self.http_method == HttpMethod.GET:
            return create_get(self.executer, self.name, self.mapper, self.serializer_class)
        elif self.http_method == HttpMethod.PUT:
            return create_put(self.serializer_class, self.executer, self.name, self.mapper)
        elif self.http_method == HttpMethod.DELETE:
            return create_delete(self.executer, self.name, self.mapper)
    
    def get_path(self) -> str:
        return self.path
    
        
def create_get(executer: Callable, name: str, mapper: SerializerMapper,
               _serializer_class: Type[Serializer] = None) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate(_serializer_class)
        def get(self, **kwargs) -> Response:
            dto = executer(**kwargs)
            return success_response(mapper.to_serializer(dto))
        def get_view_name(self):return name
    return View.as_view()

def create_post(_serializer_class: Type[Serializer],
           executer: Callable, name: str, mapper: SerializerMapper) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate(_serializer_class)
        def post(self, request: Request) -> Response:
            dto = executer(request)
            return success_response(mapper.to_serializer(dto))
        def get_view_name(self):return name
    return View.as_view()

def create_put(_serializer_class: Type[Serializer],
               executer: Callable, name: str, mapper: SerializerMapper) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate(_serializer_class)
        def put(self, request: Request) -> Response:
            dto = executer(request)
            return success_response(mapper.to_serializer(dto))
        def get_view_name(self):return name
    return View.as_view()

def create_delete(executer: Callable, name: str, mapper: SerializerMapper) -> Callable:
    class View(APIView):
        @validate()
        def delete(self, **kwargs) -> Response:
            dto = executer(**kwargs)
            return success_response(mapper.to_serializer(dto))
        def get_view_name(self):return name
    return View.as_view()