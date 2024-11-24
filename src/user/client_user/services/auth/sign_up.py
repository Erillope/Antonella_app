from src.common import override
from ...domain import ClientUserFactory, ClientUser
from ...data_providers import ClientUserRepository
from ..user_is_registered import UserIsRegistered
from ..dto import SignUpDto, ClientUserDto
from .ISign_up import ISignUp
from singleton_decorator import singleton

@singleton
class SignUp(ISignUp):
    def __init__(self, user_repository: ClientUserRepository) -> None:
        self.__user_repository = user_repository
        
    @override
    def sign_up(self, dto: SignUpDto) -> ClientUserDto:
        UserIsRegistered.verify_is_already_registered(self.__user_repository, dto.get_account())
        user = self.__register(dto)
        return ClientUserDto.generate_dto(user)
    
    def __register(self, dto: SignUpDto) -> ClientUser:
        user = ClientUserFactory.create_default(dto.get_account(), dto.get_name(), dto.get_password(), dto.get_birthdate())
        return self.__user_repository.save(user)