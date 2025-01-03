from src.common.repository import SaveModel
from src.common.repository.typing import Model
from .table_mapper import TableMapper
from django.db import models #type: ignore
from typing import Generic, TypeVar

Table = TypeVar('Table', bound=models.Model)

class DjangoSaveModel(SaveModel[Model], Generic[Table, Model]):
    def __init__(self, mapper: TableMapper[Table, Model]) -> None:
        self._mapper = mapper
    
    def save(self, model: Model) -> Model:
        table = self._mapper.to_table(model)
        table.save()
        return self._mapper.to_model(table)