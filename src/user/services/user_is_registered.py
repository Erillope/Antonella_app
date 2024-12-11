from ..data_providers import GetUser, ExistsUser
from ..domain import UserAccount
from .exception import UserIsNotRegisteredException, UserIsAlreadyRegisteredException

class UserIsRegistered:
    def __init__(self, get_user: GetUser, exists_user: ExistsUser) -> None:
        self.__get_user = get_user
        self.__exists_user = exists_user
        
    def is_registered_by_account(self, account: str) -> UserAccount:
        if self.__exists_user.exists_by_account(account):
            return self.__get_user.get_by_account(account)
        raise UserIsNotRegisteredException.is_not_registered(account)
    
    def is_registered_by_id(self, id: str) -> UserAccount:
        if self.__exists_user.exists_by_id(id):
            return self.__get_user.get_by_id(id)
        raise UserIsNotRegisteredException.is_not_registered(id)
    
    def verify_is_already_registered(self, account: str) -> None:
        if self.__exists_user.exists_by_account(account):
            raise UserIsAlreadyRegisteredException.is_already_registered(account)