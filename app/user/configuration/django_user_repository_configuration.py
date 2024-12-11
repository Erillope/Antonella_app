from src.user import UserRepositoryConfiguration, GetUser, ExistsUser, SaveUser
from ..repository import DjangoExistsUser, DjangoGetUser, DjangoSaveUser

class DjangoUserRepositoryConfiguration(UserRepositoryConfiguration):
    def construct_exists_user(self) -> ExistsUser:
        return DjangoExistsUser()
    
    def construct_get_user(self) -> GetUser:
        return DjangoGetUser(
            exists_user = self.construct_exists_user()
        )
    
    def construct_save_user(self) -> SaveUser:
        return DjangoSaveUser()