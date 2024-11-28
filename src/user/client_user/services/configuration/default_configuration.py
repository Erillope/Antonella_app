from ...data_providers import ClientUserRepositoryConfiguration
from src.user.account.services.auth import ISingIn, ISignUp
from src.user.account.services.account_data import IChangeAccountData, IEnableUserAccount, IDisableUserAccount
from src.user.account.services.auth.sign_in import SignIn
from src.user.account.services.auth.sign_up import SignUp
from src.user.account.services.account_data.change_account_data import ChangeAccountData
from src.user.account.services.account_data.enable_user_account import EnableUserAccount
from src.user.account.services.account_data.disable_user_account import DisableUserAccount
from ..client_user_mapper import ClientUserMapper
from .service_configuration import ClientUserServiceConfiguration
from singleton_decorator import singleton

@singleton
class DefaultClientUserServiceConfiguration(ClientUserServiceConfiguration):
    def __init__(self, repository_config: ClientUserRepositoryConfiguration) -> None:
        super().__init__()
        self.__user_respository = repository_config.construct_user_repository()
        self.__maper = ClientUserMapper()
    
    def construct_sign_up_service(self) -> ISignUp:
        return SignUp(self.__user_respository, self.__maper)
    
    def construct_sign_in_service(self) -> ISingIn:
        return SignIn(self.__user_respository, self.construct_enable_account_service())
    
    def construct_enable_account_service(self) -> IEnableUserAccount:
        return EnableUserAccount(self.__user_respository, self.__maper)
    
    def construct_disable_account_service(self) -> IDisableUserAccount:
        return DisableUserAccount(self.__user_respository, self.__maper)
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(self.__user_respository, self.__maper)