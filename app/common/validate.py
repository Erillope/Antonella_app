from src.common import SystemException
from .responses import failure_response, internal_server_error_response

def validate(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            if request.method == "GET" or request.method == "DELETE":
                return func(self, **kwargs)
            return func(self, request)
        except SystemException as e:
            return failure_response(e)
        #except:
        #   return internal_server_error_response()
    return wrapper