from src.user.account.services.dto import SignUpDto
from datetime import date

class ClientUserSignUpDto(SignUpDto):
    def __init__(self, account: str, name: str, password: str, birthdate: date) -> None:
        super().__init__(account, name, password)
        self.__birthdate = birthdate
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def __str__(self) -> str:
        return f"ClientUserSignUpDto(account={self.get_account()},name={self.get_name()},"\
            f"password={self.get_password()},birthdate={self.get_birthdate()})"