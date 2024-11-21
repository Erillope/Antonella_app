import re

class RegrexValidator:
    @staticmethod
    def match(pattern: str, value: str) -> bool:
        return bool(re.match(pattern, value))