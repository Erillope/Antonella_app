from ..services import (ISignUp, ISignIn, IEnableUserAccount, IDisableUserAccount,
                        IChangeAccountData, IGiveRole, IRemoveRole, IFilterUser)
from abc import ABC, abstractmethod

class UserAccountServiceConfiguration(ABC):
    @abstractmethod
    def construct_sign_up_service(self) -> ISignUp: ...
    
    @abstractmethod
    def construct_sign_in_service(self) -> ISignIn: ...
    
    @abstractmethod
    def construct_enable_account_service(self) -> IEnableUserAccount: ...
    
    @abstractmethod
    def construct_disable_account_service(self) -> IDisableUserAccount: ...
    
    @abstractmethod
    def construct_change_data_service(self) -> IChangeAccountData: ...
    
    @abstractmethod
    def construct_give_role_service(self) -> IGiveRole: ...
    
    @abstractmethod
    def construct_remove_role_service(self) -> IRemoveRole: ...
    
    @abstractmethod
    def construct_filter_user_service(self) -> IFilterUser: ...