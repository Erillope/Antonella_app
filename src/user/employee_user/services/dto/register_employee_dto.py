from typing import Set

class RegisterEmployeeDto:
    def __init__(self, account: str, name: str, roles: Set[str]) -> None:
        self.__account = account
        self.__name = name
        self.__roles = roles
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_roles(self) -> Set[str]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"RegisterEmployeeDto(account={self.get_account()},name={self.get_name()},"\
            f"roles={self.get_roles()}"