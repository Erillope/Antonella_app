class DisableDto:
    def __init__(self, id: str) -> None:
        self.__id = id.strip().lower()
    
    def get_id(self) -> str:
        return self.__id
    
    def __str__(self) -> str:
        return f"DisableDto(id={self.get_id()})"