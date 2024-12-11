from ..services import (UserIsRegistered, ISignUp, ISignIn, IEnableUserAccount, IDisableUserAccount,
                        IChangeAccountData, IGiveRole, IRemoveRole, IFilterUser)
from ..services.account_data import (ChangeAccountData, EnableUserAccount, DisableUserAccount,
                                     GiveRole, RemoveRole, FilterUser)
from ..services.auth import SignIn, SignUp
from .role_service_configuration import RoleServiceConfiguration
from .user_account_service_configuration import UserAccountServiceConfiguration
from .user_repository_configuration import UserRepositoryConfiguration

class DefaultUserAccountServiceConfiguration(UserAccountServiceConfiguration):
    def __init__(self,
                 user_repository_configuration: UserRepositoryConfiguration,
                 role_service_configuration: RoleServiceConfiguration) -> None:
        self.__user_repository_configuration = user_repository_configuration
        self.__role_service_configuration = role_service_configuration
    
    def construct_user_is_registered_service(self) -> UserIsRegistered:
        return UserIsRegistered(
            get_user = self.__user_repository_configuration.construct_get_user(),
            exists_user = self.__user_repository_configuration.construct_exists_user()
        )
    
    def construct_sign_up_service(self) -> ISignUp:
        return SignUp(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service(),
            give_role_service = self.construct_give_role_service()
        )
    
    def construct_sign_in_service(self) -> ISignIn:
        return SignIn(
            user_is_registered = self.construct_user_is_registered_service(),
            enable_account_service = self.construct_enable_account_service()
        )
    
    def construct_enable_account_service(self) -> IEnableUserAccount:
        return EnableUserAccount(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service()
        )
    
    def construct_disable_account_service(self) -> IDisableUserAccount:
        return DisableUserAccount(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service()
        )
    
    def construct_give_role_service(self) -> IGiveRole:
        return GiveRole(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service(),
            role_is_registered = self.__role_service_configuration.construct_role_is_registered_service()
        )
    
    def construct_remove_role_service(self) -> IRemoveRole:
        return RemoveRole(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service(),
            role_is_registered = self.__role_service_configuration.construct_role_is_registered_service()
        )
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(
            save_user = self.__user_repository_configuration.construct_save_user(),
            user_is_registered = self.construct_user_is_registered_service()
        )
    
    def construct_filter_user_service(self) -> IFilterUser:
        return FilterUser(
            get_user = self.__user_repository_configuration.construct_get_user()
        )