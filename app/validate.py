from src.common import SystemException
from .responses import invalid_field_response, failure_response, internal_server_error_response
from functools import wraps
from rest_framework.serializers import Serializer
from typing import Type

def validate(serializer_class: Type[Serializer] = None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if serializer_class is not None:
                serializer = serializer_class(data=request.data)
                if not serializer.is_valid(): return invalid_field_response(serializer.errors)
            try:
                if serializer_class is not None:
                    return func(self, request, **kwargs)
                return func(self, **kwargs)
            except SystemException as e:
                return failure_response(e)
            #except:
             #   return internal_server_error_response()
        return wrapper
    return decorator