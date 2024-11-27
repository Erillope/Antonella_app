from typing import Type, Callable
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from app.responses import success_response
from app.validate import validate_request, validate

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