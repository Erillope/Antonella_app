from enum import Enum

class OrdenDirection(Enum):
    ASC = "ASC"
    DESC = "DESC"

    @classmethod
    def contain_name(cls, name: str) -> bool:
        return name in cls._member_names_