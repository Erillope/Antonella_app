class StringValue:
    def __init__(self, value: str, lower: bool = True) -> None:
        self.__lower = lower
        self.__value = self.__fix(value)
    
    def __fix(self, value: str) -> str:
        value = value.strip()
        if self.__lower: 
            return value.lower()
        return value
    
    def get_value(self) -> str:
        return self.__value