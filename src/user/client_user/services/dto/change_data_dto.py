
class ChangeDataDto:
    def __init__(self, id: str, account: str, name: str, password: str) -> None:
        self.__id = id
        self.__account = account
        self.__name = name
        self.__password = password
    
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_password(self) -> str:
        return self.__password
    
    def __str__(self) -> str:
        return f"ChangeDataDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},
    password={self.get_password()})"