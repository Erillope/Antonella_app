from src.user.domain.exception import InvalidUserBirthdateException
from datetime import date

class UserBirthdate:
    __MAX_AGE = 120
    
    def __init__(self, birthdate: date) -> None:
        self.__value = birthdate
        self.__validate()
    
    def __validate(self) -> None:
        self.__validate_future_date()
        self.__validate_age()
        
    def __validate_future_date(self) -> None:
        if self.get_value() > date.today():
            raise InvalidUserBirthdateException.invalid_birthdate(self.get_value())
    
    def __validate_age(self) -> None:
        period = date.today().year - self.get_value().year
        if period > self.__MAX_AGE:
            raise InvalidUserBirthdateException.invalid_birthdate(self.get_value())
    
    def get_value(self) -> date:
        return self.__value
    
    def __str__(self) -> str:
        return str(self.__value)