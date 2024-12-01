from src.user.account import (ISingIn, IChangeAccountData, IDisableUserAccount,
                              IEnableUserAccount, UserIsRegistered)
from ..auth import IRegisterEmployee
from ..account_data import IGiveRole, ITakeRole
from ..role_is_registered import RoleIsRegistered
from ..role import IAddRole, IRemoveRole
from abc import ABC, abstractmethod

class EmployeeUserServiceConfiguration(ABC):
    @abstractmethod
    def construct_employee_is_registered_service(self) -> UserIsRegistered: ...
    
    @abstractmethod
    def construct_role_is_registered(self) -> RoleIsRegistered: ...
    
    @abstractmethod
    def construct_register_service(self) -> IRegisterEmployee: ...
    
    @abstractmethod
    def construct_sign_in_service(self) -> ISingIn: ...
    
    @abstractmethod
    def construct_enable_account_service(self) -> IEnableUserAccount: ...
    
    @abstractmethod
    def construct_disable_account_service(self) -> IDisableUserAccount: ...
    
    @abstractmethod
    def construct_change_data_service(self) -> IChangeAccountData: ...
    
    @abstractmethod
    def construct_give_role_service(self) -> IGiveRole: ...
    
    @abstractmethod
    def construct_take_role_service(self) -> ITakeRole: ...
    
    @abstractmethod
    def construct_add_role_service(self) -> IAddRole: ...
    
    @abstractmethod
    def construct_remove_role_service(self) -> IRemoveRole: ...