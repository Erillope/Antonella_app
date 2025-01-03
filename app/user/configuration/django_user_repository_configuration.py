from src.user import UserRepositoryConfiguration, GetUser, ExistsUser, SaveUser
from ..repository import DjangoExistsUser, DjangoGetUser, DjangoSaveUser

class DjangoUserRepositoryConfiguration(UserRepositoryConfiguration):
    def construct_exists_user(self) -> ExistsUser:
        return DjangoExistsUser()
    
    def construct_get_user(self) -> GetUser:
        return DjangoGetUser()
    
    def construct_save_user(self) -> SaveUser:
        return DjangoSaveUser(get_user=self.construct_get_user())