from src.user.account import AccountState
from ...domain import ClientUser
from datetime import date

class ClientUserDto:
    def __init__(self, id: str, account: str, name: str, birthdate: date, state: AccountState) -> None:
        self.__id = id
        self.__account = account
        self.__name = name
        self.__birthdate = birthdate
        self.__state = state
    
    @staticmethod
    def generate_dto(user: ClientUser) -> "ClientUserDto":
        return ClientUserDto(user.get_id(), user.get_account(), user.get_name(),
                             user.get_birthdate(), user.get_state())
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def get_state(self) -> AccountState:
        return self.__state
    
    def __str__(self) -> str:
        return f"ClientUserDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},
    birthdate={self.get_birthdate()},state={self.get_state()})"