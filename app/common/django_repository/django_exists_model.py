from src.common.repository import ExistsModel
from django.db import models #type: ignore
from typing import Type, Generic, TypeVar

Table = TypeVar('Table', bound=models.Model)

class DjangoExistsModel(ExistsModel, Generic[Table]):
    def __init__(self, table: Type[Table]) -> None:
        self._table = table
    
    def exists(self, id: str) -> bool:
        return self._table.objects.filter(id=id).exists()