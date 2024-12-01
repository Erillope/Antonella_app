from ..data_providers import GetUser, ExistsUser
from ..domain import UserAccount
from .exception import UserIsNotRegisteredException, UserIsAlreadyRegisteredException

class UserIsRegistered:
    def __init__(self, global_exists_user: ExistsUser, concrete_get_user: GetUser,
                 concrete_exists_user: ExistsUser) -> None:
        self.__global_exists_user = global_exists_user
        self.__concrete_get_user = concrete_get_user
        self.__concrete_exists_user = concrete_exists_user
        
    def is_registered_by_account(self, account: str) -> UserAccount:
        if self.__concrete_exists_user.exists_by_account(account):
            return self.__concrete_get_user.get_by_account(account)
        raise UserIsNotRegisteredException.is_not_registered(account)
    
    def is_registered_by_id(self, id: str) -> UserAccount:
        if self.__concrete_exists_user.exists_by_id(id):
            return self.__concrete_get_user.get_by_id(id)
        raise UserIsNotRegisteredException.is_not_registered(id)
    
    def verify_is_already_registered(self, account: str) -> UserAccount:
        if self.__global_exists_user.exists_by_account(account):
            raise UserIsAlreadyRegisteredException.is_already_registered(account)