from .invalid_account_exception import InvalidAccountException

class InvalidPhoneNumberException(InvalidAccountException):
    @classmethod
    def invalid_phone_number(cls, phone_number: str) -> "InvalidPhoneNumberException":
        return cls(f"El número de celular '{phone_number}' es inválido")