from src.common.exception import InvalidFieldException, MissingOperationException
from src.common import FilterExpresion, OrdenDirection, StringValue
from django.db.models import Q, Model #type: ignore
from typing import List, Type, Tuple, Optional

class BinaryExpresion:
    DJANGO_OPERATIONS = {'>': 'gt', '<': 'lt', '=': 'exact'}
    
    def __init__(self, binary_expresion: str) -> None:
        self.__expresion = StringValue(binary_expresion).get_value()
        self.__tokens = self.__get_tokens()
    
    def __get_tokens(self) -> Tuple[str, str, str]:
        for opt in self.DJANGO_OPERATIONS:
            if opt in self.__expresion:
                (self.__expresion.split(opt)[0],self.__expresion.split(opt)[1],opt)
                return (self.__expresion.split(opt)[0], self.__expresion.split(opt)[1], opt)
        raise MissingOperationException.missing_operation(list(self.DJANGO_OPERATIONS.keys()))
                        
    def get_operation(self) -> str:
        return self.DJANGO_OPERATIONS[self.__tokens[2]]
    
    def get_field(self) -> str:
        return self.__tokens[0]
    
    def get_value(self) -> str:
        return self.__tokens[1]

class DjangoFilter(FilterExpresion[Model]):    
    def __init__(self, table: Type[Model], binary_expresion: str, limit: int, offset: int,
                 order_by: str, direction: OrdenDirection, fields: List[str]) -> None:
        self.__fields = fields
        self.__filter = self.__generate_q_filter(binary_expresion)
        self.__limit = limit
        self.__offset = offset
        self.__verify_field(order_by)
        self.__order_by = order_by
        self.__direction = direction
        self.__table = table
        
    def and_(self, binary_expresion: str) -> None:
        self.__filter &= self.__generate_q_filter(binary_expresion)
    
    def or_(self, binary_expresion: str) -> None:
        self.__filter |= self.__generate_q_filter(binary_expresion) 
    
    def __generate_q_filter(self, binary_expresion: str) -> Q:
        binary_expresion = binary_expresion.lower().strip()
        if binary_expresion is None or binary_expresion == "":
            return Q()
        expresion = BinaryExpresion(binary_expresion)
        self.__verify_field(expresion.get_field())
        lookup = f"{expresion.get_field()}__{expresion.get_operation()}"
        return Q(**{lookup: expresion.get_value()})
    
    def __verify_field(self, field: str) -> None:
        if field not in self.__fields:
            raise InvalidFieldException.invalid_field(field, self.__fields)

    def filter(self) -> List[Model]:
        models = self.__table.objects.filter(self.__filter)
        if self.__direction == OrdenDirection.DESC:
            models = models.order_by(f"-{self.__order_by}")
        return models[self.__offset: self.__offset+self.__limit]
    
    @classmethod
    def construct_filter(cls, table: Type[Model], expresion: Optional[str], limit: int, offset: int,
                 order_by: str, direction: OrdenDirection, fields: List[str]) -> "DjangoFilter":
        if expresion is None or expresion.strip() == "":
            expresion = ""
        expresion = expresion.lower().strip().replace(' ', ',')
        exps = expresion.split(',')
        _filter = cls(table, exps[0], limit, offset, order_by, direction, fields)
        for i in range(1, len(exps)-2, 2):
            if exps[i] == "and":
                _filter.and_(exps[i+1])
            if exps[i] == "or":
                _filter.or_(exps[i+1])
        return _filter