from ...data_providers import EmployeeUserRepositoryConfiguration
from .service_configuration import EmployeeUserServiceConfiguration
from ..auth import ISingIn, IRegisterEmployee
from ..account_data import (IChangeAccountData, IDisableEmployeeUserAccount, IEnableEmployeeUserAccount,
                            IGiveRole, ITakeRole)
from ..role import IAddRole, IRemoveRole
from ..auth.register_employee import RegisterEmployee
from ..auth.sign_in import SignIn
from ..account_data.change_account_data import ChangeAccountData
from ..account_data.disable_employee_user_account import DisableEmployeeUserAccount
from ..account_data.enable_employee_user_account import EnableEmployeeUserAccount
from ..account_data.give_role import GiveRole
from ..account_data.take_role import TakeRole
from ..role.add_role import AddRole
from ..role.remove_role import RemoveRole
from singleton_decorator import singleton

@singleton
class DefaultEmployeeUserServiceConfiguration(EmployeeUserServiceConfiguration):
    def __init__(self, repository_config: EmployeeUserRepositoryConfiguration) -> None:
        self.__employee_repository = repository_config.construct_employee_repository()
        self.__role_repository = repository_config.construct_role_repository()
        
    def construct_register_service(self) -> IRegisterEmployee:
        return RegisterEmployee(self.__employee_repository, self.__role_repository,
                                self.construct_give_role_service())
    
    def construct_sign_in_service(self) -> ISingIn:
        return SignIn(self.__employee_repository, self.construct_enable_account_service())
    
    def construct_enable_account_service(self) -> IEnableEmployeeUserAccount:
        return EnableEmployeeUserAccount(self.__employee_repository)
    
    def construct_disable_account_service(self) -> IDisableEmployeeUserAccount:
        return DisableEmployeeUserAccount(self.__employee_repository)
    
    def construct_change_data_service(self) -> IChangeAccountData:
        return ChangeAccountData(self.__employee_repository)
    
    def construct_give_role_service(self) -> IGiveRole:
        return GiveRole(self.__employee_repository, self.__role_repository)
    
    def construct_take_role_service(self) -> ITakeRole:
        return TakeRole(self.__employee_repository)
    
    def construct_add_role_service(self) -> IAddRole:
        return AddRole(self.__role_repository)
    
    def construct_remove_role_service(self) -> IRemoveRole:
        return RemoveRole(self.__role_repository)