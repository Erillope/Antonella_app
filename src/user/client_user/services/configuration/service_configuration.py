from ..auth import ISingIn, ISignUp
from ..account_data import IEnableClientUserAccount, IDisableClientUserAccount, IChangeAccountData
from abc import ABC, abstractmethod

class ClientUserServiceConfiguration(ABC):
    @abstractmethod
    def construct_sign_up_service(self) -> ISignUp: ...
    
    @abstractmethod
    def construct_sign_in_service(self) -> ISingIn: ...
    
    @abstractmethod
    def construct_enable_account_service(self) -> IEnableClientUserAccount: ...
    
    @abstractmethod
    def construct_disable_account_service(self) -> IDisableClientUserAccount: ...
    
    @abstractmethod
    def construct_change_data_service(self) -> IChangeAccountData: ...