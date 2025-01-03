from app.user.serializers import SignInSerializer, SignUpSerializer, UserSerializer
from app.user.configuration import DependenciesManager
from app.common.controller import Controller
from .user_request_mapper import UserRequestMapper
from .user_serializer_mapper import UserSerializerMapper

class AuthController(Controller):
    controller_route = "auth"
    services = DependenciesManager.get_user_services()
    request_mapper = UserRequestMapper()
    serializer_mapper = UserSerializerMapper()
    
    @Controller.post("signup", "Sign Up", SignUpSerializer)
    def sign_up(cls, request: SignUpSerializer) -> UserSerializer:
        sign_up_service = cls.services.construct_sign_up_service()
        dto = sign_up_service.sign_up(cls.request_mapper.to_sign_up_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.post("signin", "Sign In", SignInSerializer)
    def sign_in(cls, request: SignInSerializer) -> UserSerializer:
        sign_in_service = cls.services.construct_sign_in_service()
        dto = sign_in_service.sign_in(cls.request_mapper.to_sign_in_dto(request))
        return cls.serializer_mapper.to_serializer(dto)