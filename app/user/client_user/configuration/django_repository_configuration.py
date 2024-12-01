from src.user.account.data_providers import UserRepositoryConfiguration
from src.user.account.data_providers import ExistsUser, GetUser, SaveUser
from ..repository import DjangoSaveClientUser, DjangoExistsClientUser, DjangoGetClientUser
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepositoryConfiguration(UserRepositoryConfiguration):
    def construct_exists_user(self) -> ExistsUser:
        return DjangoExistsClientUser()
    
    def construct_get_user(self) -> GetUser:
        return DjangoGetClientUser(
            exists_client_user = self.construct_exists_user()
        )
    
    def construct_save_user(self) -> SaveUser:
        return DjangoSaveClientUser()