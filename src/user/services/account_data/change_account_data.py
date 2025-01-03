from src.user.data_providers import SaveUser, GetUser, ExistsUser
from src.user.domain import UserAccount
from ..dto import UserAccountDto, ChangeDataDto
from ..exception import UserIsAlreadyRegisteredException
from ..mapper import UserAccountMapper
from .abstract_change_account_data import IChangeAccountData

class ChangeAccountData(IChangeAccountData):
    def __init__(self, save_user: SaveUser, get_user: GetUser, exists_user: ExistsUser) -> None:
        self.__get_user = get_user
        self.__exists_user = exists_user
        self.__save_user = save_user
        self.__mapper = UserAccountMapper()
        
    def change_data(self, dto: ChangeDataDto) -> UserAccountDto:
        user = self.__verify(dto)
        user = self.__change(user, dto)
        roles = self.__get_user.get_roles(user.get_id())
        return self.__mapper.to_dto(user, roles)
        
    def __change(self, user: UserAccount, dto: ChangeDataDto) -> UserAccount:
        account = dto.get_account()
        name = dto.get_name()
        password = dto.get_password()
        if account is not None:
            user.change_account(account)
        if name is not None:
            user.change_name(name)
        if password is not None:
            user.change_password(password)
        return self.__save_user.save(user)
    
    def __verify(self, dto: ChangeDataDto) -> UserAccount:
        user = self.__get_user.get_by_id(dto.get_id())
        account = dto.get_account()
        if account is not None and not user.is_my_account(account):
            if self.__exists_user.exists_by_account(account):
                raise UserIsAlreadyRegisteredException.is_already_registered(account)
        return user