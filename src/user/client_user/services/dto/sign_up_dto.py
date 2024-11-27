from datetime import date

class SignUpDto:
    def __init__(self, account: str, name: str, password: str, birthdate: date) -> None:
        self.__account = account.strip()
        self.__name = name.strip()
        self.__password = password
        self.__birthdate = birthdate
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_password(self) -> str:
        return self.__password
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def __str__(self) -> str:
        return f"SignUpDto(account={self.get_account()},name={self.get_name()},password={self.get_password()},"\
    f"birthdate={self.get_birthdate()})"