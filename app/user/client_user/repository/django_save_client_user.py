from src.user.account.data_providers import SaveUser
from src.user.client_user.domain import ClientUser
from .client_user_table_mapper import ClientUserTableMapper
from singleton_decorator import singleton

@singleton
class DjangoSaveClientUser(SaveUser):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = ClientUserTableMapper()
        
    def save(self, user: ClientUser) -> ClientUser:
        user_table = self.__mapper.to_table(user)
        user_table.save()
        saved_user = self.__mapper.to_user(user_table)
        return saved_user