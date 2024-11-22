from ..data_providers import ClientUserRepository
from ..domain import ClientUser
from .exception import UserIsNotRegisteredException, UserIsAlreadyRegisteredException

class UserIsRegistered:
    @staticmethod
    def is_registered_by_account(user_repository: ClientUserRepository, account: str) -> ClientUser:
        if user_repository.exists_by_account(account):
            return user_repository.get_by_account(account)
        raise UserIsNotRegisteredException.is_not_registered(account)
    
    @staticmethod
    def is_registered_by_id(user_repository: ClientUserRepository, id: str) -> ClientUser:
        if user_repository.exists_by_id(id):
            return user_repository.get_by_id(id)
        raise UserIsNotRegisteredException.is_not_registered(id)
    
    @staticmethod
    def verify_is_already_registered(user_repository: ClientUserRepository, account: str) -> ClientUser:
        if user_repository.exists_by_account(account):
            raise UserIsAlreadyRegisteredException.is_already_registered(account)