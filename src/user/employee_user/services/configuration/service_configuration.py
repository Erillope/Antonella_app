from ..auth import ISingIn, IRegisterEmployee
from ..account_data import (IChangeAccountData, IDisableEmployeeUserAccount, IEnableEmployeeUserAccount,
                            IGiveRole, ITakeRole)
from ..role import IAddRole, IRemoveRole
from abc import ABC, abstractmethod

class EmployeeUserServiceConfiguration(ABC):
    @abstractmethod
    def construct_register_service(self) -> IRegisterEmployee: ...
    
    @abstractmethod
    def construct_sign_in_service(self) -> ISingIn: ...
    
    @abstractmethod
    def construct_enable_account_service(self) -> IEnableEmployeeUserAccount: ...
    
    @abstractmethod
    def construct_disable_account_service(self) -> IDisableEmployeeUserAccount: ...
    
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