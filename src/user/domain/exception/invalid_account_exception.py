from .user_exception import UserException

class InvalidAccountException(UserException):        
    @classmethod
    def invalid_account(cls, account: str) -> "InvalidAccountException":
        return cls(f"La cuenta '{account}' es inválida")