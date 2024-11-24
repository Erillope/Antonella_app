from .invalid_account_exception import InvalidAccountException

class InvalidPhoneNumberException(InvalidAccountException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        
    @staticmethod
    def invalid_phone_number(phone_number: str) -> "InvalidPhoneNumberException":
        return InvalidPhoneNumberException(f"El número de celular '{phone_number}' es inválido")