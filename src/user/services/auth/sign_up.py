from src.user.domain import UserAccount
from ...data_providers import SaveUser
from ..account_data import IGiveRole
from ..user_is_registered import UserIsRegistered
from ..dto import SignUpDto, UserAccountDto, GiveRoleDto
from .abstract_sign_up import ISignUp
from ..user_account_mapper import UserAccountMapper

class SignUp(ISignUp):
    def __init__(self, save_user: SaveUser, user_is_registered: UserIsRegistered,
                 give_role_service: IGiveRole) -> None:
        self.__user_is_registered = user_is_registered
        self.__save_user = save_user
        self.__give_role_service = give_role_service
        self.__mapper = UserAccountMapper()
        
    def sign_up(self, dto: SignUpDto) -> UserAccountDto:
        self.__user_is_registered.verify_is_already_registered(dto.get_account())
        user = self.__register(dto)
        user_dto = self.__give_role(user, dto)
        return user_dto
    
    def __register(self, dto: SignUpDto) -> UserAccount:
        user = self.__mapper.to_user(dto)
        return self.__save_user.save(user)
    
    def __give_role(self, user: UserAccount, dto: SignUpDto) -> UserAccountDto:
        roles = dto.get_roles()
        if roles is not None:
            user_dto = self.__give_role_service.give(GiveRoleDto(user.get_id(), roles))
            return user_dto
        return self.__mapper.to_dto(user)