from src.common.repository import DeleteModel
from src.common.repository.typing import Model
from .table_mapper import TableMapper
from .model_not_found_exception import ModelNotFoundException
from django.db import models #type: ignore
from typing import Type, TypeVar, Generic

Table = TypeVar('Table', bound=models.Model)

class DjangoDeleteModel(DeleteModel[Model], Generic[Table, Model]):
    def __init__(self, table: Type[Table], mapper: TableMapper[Table, Model]) -> None:
        self._mapper = mapper
        self._table = table
    
    def delete(self, id: str) -> Model:
        if not self._table.objects.filter(id=id).exists():
            raise ModelNotFoundException.not_found(id)
        table = self._table.objects.get(id=id)
        table.delete()
        return self._mapper.to_model(table)