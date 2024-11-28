from ...data_providers import UserAccountRepository
from ...domain import UserAccount
from ..dto import ChangeDataDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..user_account_mapper import UserAccountMapper
from .IChange_account_data import IChangeAccountData

class ChangeAccountData(IChangeAccountData):
    def __init__(self, user_repository: UserAccountDto, mapper: UserAccountMapper) -> None:
        self.__user_repository = user_repository
        self.__mapper = mapper
        
    def change_data(self, dto: ChangeDataDto) -> UserAccountDto:
        user = self.__verify(dto)
        user = self.__change(user, dto)
        return self.__mapper.to_dto(user)
        
    def __change(self, user: UserAccount, dto: ChangeDataDto) -> UserAccountDto:
        user.change_account(dto.get_account())
        user.change_name(dto.get_name())
        user.change_password(dto.get_password())
        return self.__user_repository.save(user)
    
    def __verify(self, dto: ChangeDataDto) -> UserAccount:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        if dto.get_account() != None and not user.is_my_account(dto.get_account()):
            UserIsRegistered.verify_is_already_registered(self.__user_repository, dto.get_account())
        return user