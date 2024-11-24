from .responses import invalid_field_response, failure_response
from functools import wraps
from rest_framework.serializers import Serializer
from typing import Type

def validate(serializer_class: Type[Serializer], exception_class: Type[Exception]):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            serializer = serializer_class(data=request.data)
            if not serializer.is_valid(): return invalid_field_response(serializer.errors)
            try:
                return func(self, request, *args, **kwargs)
            except exception_class as e:
                return failure_response(e)
        return wrapper
    return decorator