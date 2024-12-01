from ...data_providers import EmployeeUserRepositoryConfiguration
from .service_configuration import EmployeeUserServiceConfiguration
from src.user.account import (ISingIn, IChangeAccountData,
                              IDisableUserAccount, IEnableUserAccount, UserIsRegistered)
from src.user.account.data_providers import ExistsUser
from ..auth import IRegisterEmployee
from ..account_data import IGiveRole, ITakeRole
from ..role import IAddRole, IRemoveRole
from ..auth.register_employee import RegisterEmployee
from src.user.account.services.auth.sign_in import SignIn
from src.user.account.services.account_data.change_account_data import ChangeAccountData
from src.user.account.services.account_data.disable_user_account import DisableUserAccount
from src.user.account.services.account_data.enable_user_account import EnableUserAccount
from ..employee_user_mapper import EmployeeUserMapper
from ..account_data.give_role import GiveRole
from ..account_data.take_role import TakeRole
from ..role_is_registered import RoleIsRegistered
from ..role.add_role import AddRole
from ..role.remove_role import RemoveRole
from singleton_decorator import singleton

@singleton
class DefaultEmployeeUserServiceConfiguration(EmployeeUserServiceConfiguration):
    def __init__(self, global_exists_user: ExistsUser,
                 employee_user_repository_config: EmployeeUserRepositoryConfiguration) -> None:
        super().__init__()
        self.__get_employee_user = employee_user_repository_config.construct_get_user()
        self.__exists_employee_user = employee_user_repository_config.construct_exists_user()
        self.__save_employee_user = employee_user_repository_config.construct_save_user()
        self.__global_exists_user = global_exists_user
        self.__get_role = employee_user_repository_config.construct_get_role()
        self.__delete_role = employee_user_repository_config.construct_delete_role()
        self.__save_role = employee_user_repository_config.construct_save_role()
        self.__mapper = EmployeeUserMapper()
    
    def construct_employee_is_registered_service(self) -> UserIsRegistered:
        return UserIsRegistered(
            global_exists_user = self.__global_exists_user,
            concrete_get_user = self.__get_employee_user,
            concrete_exists_user = self.__exists_employee_user
        )
    
    def construct_role_is_registered(self) -> RoleIsRegistered:
        return RoleIsRegistered(
            get_role = self.__get_role
        )
    
    def construct_register_service(self) -> IRegisterEmployee:
        return RegisterEmployee(
            save_employee = self.__save_employee_user,
            give_role_service = self.construct_give_role_service(),
            employee_is_registered = self.construct_employee_is_registered_service(),
            role_is_registered = self.construct_role_is_registered()
            )
    
    def construct_sign_in_service(self) -> ISingIn:
        return SignIn(
            user_is_registered = self.construct_employee_is_registered_service(),
            enable_account_service = self.construct_enable_account_service()
        )
    
    def construct_enable_account_service(self) -> IEnableUserAccount:
        return EnableUserAccount(
            save_user = self.__save_employee_user,
            user_is_registered = self.construct_employee_is_registered_service(),
            mapper = self.__mapper
        )
    
    def construct_disable_account_service(self) -> IDisableUserAccount:
        return DisableUserAccount(
            save_user = self.__save_employee_user,
            user_is_registered = self.construct_employee_is_registered_service(),
            mapper = self.__mapper
        )
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(
            save_user = self.__save_employee_user,
            user_is_registered = self.construct_employee_is_registered_service(),
            mapper = self.__mapper
        )
    
    def construct_give_role_service(self) -> IGiveRole:
        return GiveRole(
            save_employee = self.__save_employee_user,
            employee_is_registered = self.construct_employee_is_registered_service(),
            role_is_registered = self.construct_role_is_registered()
        )
    
    def construct_take_role_service(self) -> ITakeRole:
        return TakeRole(
            save_employee = self.__save_employee_user,
            employee_is_registered = self.construct_employee_is_registered_service()
        )
    
    def construct_add_role_service(self) -> IAddRole:
        return AddRole(
            save_role = self.__save_role,
            role_is_registered = self.construct_role_is_registered()
        )
    
    def construct_remove_role_service(self) -> IRemoveRole:
        return RemoveRole(
            delete_role = self.__delete_role,
            role_is_registered = self.construct_role_is_registered()
        )