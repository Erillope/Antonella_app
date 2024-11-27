class EnableDto:
    def __init__(self, id: str) -> None:
        self.__id = id.strip()
    
    def get_id(self) -> str:
        return self.__id
    
    def __str__(self) -> str:
        return f"EnableDto(id={self.get_id()})"