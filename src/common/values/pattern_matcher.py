import re

class PatternMatcher:
    def __init__(self, pattern: str) -> None:
        self.__pattern = pattern
        
    def match(self, value: str) -> bool:
        return bool(re.match(self.__pattern, value))