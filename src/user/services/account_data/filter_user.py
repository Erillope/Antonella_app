from src.user.data_providers import GetUser
from .abstract_filter_user import IFilterUser
from ..dto import FilterUserDto, UserAccountDto
from ..user_account_mapper import UserAccountMapper
from typing import List

class FilterUser(IFilterUser):
    def __init__(self, get_user: GetUser) -> None:
        self.__get_user = get_user
        self.__mapper = UserAccountMapper()
        
    def filter(self, dto: FilterUserDto) -> List[UserAccountDto]:
        users = self.__get_user.filter(
            expresion = dto.get_expresion(),
            limit = dto.get_limit(),
            offset = dto.get_offset(),
            order_by = dto.get_order_by(),
            direction = dto.get_direction()
        )
        dtos = [self.__mapper.to_dto(user) for user in users]
        return dtos
