from src.user.account import AccountStatus
from ...domain import ClientUser
from datetime import date

class ClientUserDto:
    def __init__(self, id: str, account: str, name: str, birthdate: date, status: AccountStatus, joined_date: date) -> None:
        self.__id = id
        self.__account = account
        self.__name = name
        self.__birthdate = birthdate
        self.__status = status
        self.__joined_date = joined_date
    
    @staticmethod
    def generate_dto(user: ClientUser) -> "ClientUserDto":
        return ClientUserDto(user.get_id(), user.get_account(), user.get_name(),
                             user.get_birthdate(), user.get_status(), user.get_joined_date())
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def get_status(self) -> AccountStatus:
        return self.__status
    
    def get_joined_date(self) -> date:
        return self.__joined_date
    
    def __str__(self) -> str:
        return f"ClientUserDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"birthdate={self.get_birthdate()},status={self.get_status()},joined_date={self.get_joined_date()})"