from ....common import raises
from ..exception import InvalidUserIDException
import uuid

class UserID:
    @raises(InvalidUserIDException)
    def __init__(self, id: str) -> None:
        self.__validate_id(id)
        self.__value = id
    
    @raises(InvalidUserIDException)
    def __validate_id(self, id: str) -> None:
        try:
            uuid.UUID(id)
        except:
            raise InvalidUserIDException.invalid_user_id()
    
    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserID):
            return self.value == value.value
        return False
    
    def __hash__(self) -> int:
        return hash(self.value)