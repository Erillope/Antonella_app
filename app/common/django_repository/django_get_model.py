from src.common import OrdenDirection
from src.common.repository import GetModel
from src.common.repository.typing import Model
from .table_mapper import TableMapper
from app.common.django_repository.filter import DjangoFilter
from .model_not_found_exception import ModelNotFoundException
from django.db import models #type: ignore
from typing import Type, List, Optional, TypeVar, Generic

Table = TypeVar('Table', bound=models.Model)

class DjangoGetModel(GetModel[Model], Generic[Table, Model]):
    def __init__(self, table: Type[Table], mapper: TableMapper[Table, Model]) -> None:
        self._table = table
        self._mapper = mapper
        self.__allowed_fields : List[str] = []
        
    def get_all(self) ->List[Model]:
        tables = self._table.objects.all()
        return [self._mapper.to_model(table) for table in tables]
    
    def get_by_id(self, id: str) -> Model:
        if not self._table.objects.filter(id=id).exists():
            raise ModelNotFoundException.not_found(id)
        table = self._table.objects.get(id=id)
        return self._mapper.to_model(table)
    
    def filter(self, expresion: Optional[str], limit: int, offset: int,
               order_by: str, direction: OrdenDirection) -> List[Model]:
        _filter = DjangoFilter.construct_filter(self._table, expresion, limit, offset,
                                                order_by, direction, self.__allowed_fields)
        tables = _filter.filter()
        return [self._mapper.to_model(table) for table in tables]
    
    def set_allowed_fields(self, fields: List[str]) -> None:
        self.__allowed_fields = fields