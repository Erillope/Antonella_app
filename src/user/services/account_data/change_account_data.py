from src.user.data_providers import SaveUser
from src.user.domain import UserAccount
from ..dto import ChangeDataDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..user_account_mapper import UserAccountMapper
from .abstract_change_account_data import IChangeAccountData

class ChangeAccountData(IChangeAccountData):
    def __init__(self, save_user: SaveUser, user_is_registered: UserIsRegistered) -> None:
        self.__user_is_registered = user_is_registered
        self.__save_user = save_user
        self.__mapper = UserAccountMapper()
        
    def change_data(self, dto: ChangeDataDto) -> UserAccountDto:
        user = self.__verify(dto)
        user = self.__change(user, dto)
        return self.__mapper.to_dto(user)
        
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
        user = self.__user_is_registered.is_registered_by_id(dto.get_id())
        account = dto.get_account()
        if account is not None and not user.is_my_account(account):
            self.__user_is_registered.verify_is_already_registered(account)
        return user