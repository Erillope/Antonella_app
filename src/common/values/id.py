from src.common.exception import InvalidIdException
from src.common.values.string_value import StringValue
import uuid

class ID:
    def __init__(self, value: str) -> None:
        self.__value = StringValue(value)
        self.__validate()
    
    def __validate(self) -> None:
        try:
            uuid.UUID(self.__value.get_value())
        except:
            raise InvalidIdException.invalid_id(self.__value.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())