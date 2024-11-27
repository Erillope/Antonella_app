from typing import Type, Callable
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from app.responses import success_response
from app.validate import validate_request, validate
from enum import Enum

class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    
class ViewCreator:
    def __init__(self, path: str, exception_class: Type[Exception] ,executer: Callable,
                 name: str, http_method: HttpMethod, serializer_class: Type[Serializer] = None) -> None:
        self.path = path
        self.serializer_class = serializer_class
        self.exception_class = exception_class
        self.executer = executer
        self.name = name
        self.http_method = http_method
        
    def create(self) -> Callable:
        if self.http_method == HttpMethod.POST:
            return create_post(self.serializer_class, self.exception_class, self.executer, self.name)
        elif self.http_method == HttpMethod.GET:
            return create_get(self.serializer_class, self.exception_class, self.executer, self.name)
        elif self.http_method == HttpMethod.PUT:
            return create_put(self.serializer_class, self.exception_class, self.executer, self.name)
        elif self.http_method == HttpMethod.DELETE:
            return create_delete(self.exception_class, self.executer, self.name)
    
    def get_path(self) -> str:
        return self.path
    
        
def create_get(_serializer_class: Type[Serializer], exception_class: Type[Exception]
               , executer: Callable, name: str) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate_request(_serializer_class, exception_class)
        def get(self, request: Request) -> Response:
            serializer = executer(request)
            return success_response(serializer)
        def get_view_name(self):return name
    return View.as_view()

def create_post(_serializer_class: Type[Serializer], exception_class: Type[Exception],
           executer: Callable, name: str) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate_request(_serializer_class, exception_class)
        def post(self, request: Request) -> Response:
            serializer = executer(request)
            return success_response(serializer)
        def get_view_name(self):return name
    return View.as_view()

def create_put(_serializer_class: Type[Serializer], exception_class: Type[Exception],
           executer: Callable, name: str) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate_request(_serializer_class, exception_class)
        def put(self, request: Request) -> Response:
            serializer = executer(request)
            return success_response(serializer)
        def get_view_name(self):return name
    return View.as_view()

def create_delete(exception_class: Type[Exception],
           executer: Callable, name: str) -> Callable:
    class View(APIView):
        @validate(exception_class)
        def delete(self, **kwargs) -> Response:
            serializer = executer(**kwargs)
            return success_response(serializer)
        def get_view_name(self):return name
    return View.as_view()