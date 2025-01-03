from src.common import StringValue

class SignInDto:
    def __init__(self, account: str, password: str) -> None:
        self.__account = StringValue(account)
        self.__password = password
    
    def get_account(self) -> str:
        return self.__account.get_value()
    
    def get_password(self) -> str:
        return self.__password
    
    def __str__(self) -> str:
        return f"SignInDto(account={self.get_account()},password={self.get_password()})"