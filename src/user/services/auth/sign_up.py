from src.common.repository import ExistsModel
from src.user.data_providers import ExistsUser
from src.user.domain import UserAccount
from src.user.data_providers import SaveUser
from ..exception import UserIsAlreadyRegisteredException, RoleIsNotRegisteredException
from ..account_data import IGiveRole
from ..dto import SignUpDto, GiveRoleDto, UserAccountDto
from .abstract_sign_up import ISignUp
from ..mapper import UserAccountMapper

class SignUp(ISignUp):
    def __init__(self, save_user: SaveUser, exists_user: ExistsUser,
                 exists_role: ExistsModel, give_role_service: IGiveRole) -> None:
        self.__exists_user = exists_user
        self.__exists_role = exists_role
        self.__save_user = save_user
        self.__give_role_service = give_role_service
        self.__mapper = UserAccountMapper()
        
    def sign_up(self, dto: SignUpDto) -> UserAccountDto:
        self.__verify_is_registered(dto)
        user = self.__register(dto)
        user_dto = self.__give_role(user, dto)
        return user_dto
    
    def __verify_is_registered(self, dto: SignUpDto) -> None:
        if self.__exists_user.exists_by_account (dto.get_account()):
            raise UserIsAlreadyRegisteredException.is_already_registered(dto.get_account())
        roles = dto.get_roles()
        if roles is not None:
            for role in roles:
                if not self.__exists_role.exists(role):
                    raise RoleIsNotRegisteredException.is_not_registered(role)
            
    def __register(self, dto: SignUpDto) -> UserAccount:
        user = self.__mapper.to_user(dto)
        return self.__save_user.save(user)
    
    def __give_role(self, user: UserAccount, dto: SignUpDto) -> UserAccountDto:
        roles = dto.get_roles()
        if roles is not None:
            user_dto = self.__give_role_service.give(GiveRoleDto(user.get_id(), roles))
            return user_dto
        return self.__mapper.to_dto(user, [])