from typing import Type, Callable
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.request import Request
from rest_framework.response import Response
from app.common.responses import success_response
from app.common.validate import validate
from app.common.serializer_mapper import SerializerMapper
        
def create_get(executer: Callable, name: str) -> Callable:
    class View(APIView):
        @validate
        def get(self, **kwargs) -> Response:
            return success_response(executer.do(**kwargs))
        def get_view_name(self):return name
    return View.as_view()

def create_post(_serializer_class: Type[Serializer], executer: Callable, name: str) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate
        def post(self, request: Request) -> Response:
            return success_response(executer.do(request))
        def get_view_name(self):return name
    return View.as_view()

def create_put(_serializer_class: Type[Serializer],
               executer: Callable, name: str) -> Callable:
    class View(APIView):
        serializer_class = _serializer_class
        @validate
        def put(self, request: Request) -> Response:
            return success_response(executer.do(request))
        def get_view_name(self):return name
    return View.as_view()

def create_delete(executer: Callable, name: str) -> Callable:
    class View(APIView):
        @validate
        def delete(self, **kwargs) -> Response:
            return success_response(executer.do(**kwargs))
        def get_view_name(self):return name
    return View.as_view()