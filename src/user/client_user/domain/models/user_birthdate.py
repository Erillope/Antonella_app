from ..exception import InvalidUserBirthdateException
from datetime import date

class UserBirthdate:
    __MAX_AGE = 120
    
    def __init__(self, birthdate: date) -> None:
        self.__validate(birthdate)
        self.__value = date
    
    def __validate(self, birthdate: date) -> None:
        self.__validate_future_date(birthdate)
        self.__validate_age(birthdate)
        
    def __validate_future_date(self, birthdate: date) -> None:
        if birthdate < date.today():
            raise InvalidUserBirthdateException.invalid_birthdate(birthdate)
    
    def __validate_age(self, birthdate: date) -> None:
        period = date.today().year - birthdate.year
        if period > self.__MAX_AGE:
            raise InvalidUserBirthdateException.invalid_birthdate(birthdate)
    
    def get_value(self) -> date:
        return self.__value
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserBirthdate):
            return self.__value == value.__value
        return False
    
    def __hash__(self) -> int:
        return hash(self.__value)