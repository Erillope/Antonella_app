from src.user.account.data_providers import UserRepositoryConfiguration, ExistsUser
from src.user.account import (ISingIn, ISignUp, IChangeAccountData, IEnableUserAccount,
                              IDisableUserAccount, UserIsRegistered, UserServiceConfiguration)
from src.user.account.services.auth.sign_in import SignIn
from src.user.account.services.auth.sign_up import SignUp
from src.user.account.services.account_data.change_account_data import ChangeAccountData
from src.user.account.services.account_data.enable_user_account import EnableUserAccount
from src.user.account.services.account_data.disable_user_account import DisableUserAccount
from ..client_user_mapper import ClientUserMapper
from singleton_decorator import singleton

@singleton
class DefaultClientUserServiceConfiguration(UserServiceConfiguration):
    def __init__(self, global_exists_user: ExistsUser,
                 client_user_repository_config: UserRepositoryConfiguration) -> None:
        super().__init__()
        self.__get_client_user = client_user_repository_config.construct_get_user()
        self.__exists_client_user = client_user_repository_config.construct_exists_user()
        self.__save_client_user = client_user_repository_config.construct_save_user()
        self.__global_exists_user = global_exists_user
        self.__maper = ClientUserMapper()
    
    def construct_user_is_registered_service(self) -> UserIsRegistered:
        return UserIsRegistered(
            global_exists_user = self.__global_exists_user,
            concrete_get_user = self.__get_client_user,
            concrete_exists_user = self.__exists_client_user
        )
    
    def construct_sign_up_service(self) -> ISignUp:
        return SignUp(
            save_user = self.__save_client_user,
            user_is_registered = self.construct_user_is_registered_service(),
            mapper = self.__maper
        )
    
    def construct_sign_in_service(self) -> ISingIn:
        return SignIn(
            user_is_registered = self.construct_user_is_registered_service(),
            enable_account_service = self.construct_enable_account_service()
        )
    
    def construct_enable_account_service(self) -> IEnableUserAccount:
        return EnableUserAccount(
            save_user = self.__save_client_user,
            user_is_registered = self.construct_user_is_registered_service(),
            mapper = self.__maper
        )
    
    def construct_disable_account_service(self) -> IDisableUserAccount:
        return DisableUserAccount(
            save_user = self.__save_client_user,
            user_is_registered = self.construct_user_is_registered_service(),
            mapper = self.__maper
        )
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(
            save_user = self.__save_client_user,
            user_is_registered = self.construct_user_is_registered_service(),
            mapper = self.__maper
        )