from ..exception import InvalidUserIDException
import uuid

class UserID:
    def __init__(self, id: str) -> None:
        id = id.strip()
        self.__validate_id(id)
        self.__value = id
    
    def __validate_id(self, id: str) -> None:
        try:
            uuid.UUID(id)
        except:
            raise InvalidUserIDException.invalid_user_id(id)
    
    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserID):
            return self.__value == value.__value
        return False
    
    def __hash__(self) -> int:
        return hash(self.__value)