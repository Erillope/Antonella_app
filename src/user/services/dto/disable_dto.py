from src.common import StringValue

class DisableDto:
    def __init__(self, id: str) -> None:
        self.__id = StringValue(id)
    
    def get_id(self) -> str:
        return self.__id.get_value()
    
    def __str__(self) -> str:
        return f"DisableDto(id={self.get_id()})"