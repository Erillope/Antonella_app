from src.user.account import IEnableUserAccount, IDisableUserAccount, IChangeAccountData, ISingIn, ISignUp
from abc import ABC, abstractmethod

class ClientUserServiceConfiguration(ABC):
    @abstractmethod
    def construct_sign_up_service(self) -> ISignUp: ...
    
    @abstractmethod
    def construct_sign_in_service(self) -> ISingIn: ...
    
    @abstractmethod
    def construct_enable_account_service(self) -> IEnableUserAccount: ...
    
    @abstractmethod
    def construct_disable_account_service(self) -> IDisableUserAccount: ...
    
    @abstractmethod
    def construct_change_data_service(self) -> IChangeAccountData: ...