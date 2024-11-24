from ...data_providers import ClientUserRepositoryConfiguration
from ..auth import ISingIn, ISignUp
from ..account_data import IChangeAccountData, IEnableClientUserAccount, IDisableClientUserAccount
from ..auth.sign_in import SignIn
from ..auth.sign_up import SignUp
from ..account_data.change_account_data import ChangeAccountData
from ..account_data.enable_client_user_account import EnableClientUserAccount
from ..account_data.disable_client_user_account import DisableClientUserAccount
from .service_configuration import ClientUserServiceConfiguration
from singleton_decorator import singleton

@singleton
class DefaultClientUserServiceConfiguration(ClientUserServiceConfiguration):
    def __init__(self, repository_config: ClientUserRepositoryConfiguration) -> None:
        super().__init__()
        self.__user_respository = repository_config.construct_user_repository()
    
    def construct_sign_up_service(self) -> ISignUp:
        return SignUp(self.__user_respository)
    
    def construct_sign_in_service(self) -> ISingIn:
        return SignIn(self.__user_respository, self.construct_enable_account_service())
    
    def construct_enable_account_service(self) -> IEnableClientUserAccount:
        return EnableClientUserAccount(self.__user_respository)
    
    def construct_disable_account_service(self) -> IDisableClientUserAccount:
        return DisableClientUserAccount(self.__user_respository)
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(self.__user_respository)