from src.user import SaveUser, UserAccount, Role, GetUser
from app.common.django_repository import DjangoSaveModel
from .tables import UserAccountTableData, UserTableMapper, UserRoleTableData, RoleTableMapper
from typing import List

class DjangoSaveUser(SaveUser, DjangoSaveModel[UserAccountTableData, UserAccount]):
    def __init__(self, get_user: GetUser) -> None:
        super().__init__(UserTableMapper())
        self.__get_user = get_user
        self.__role_mapper = RoleTableMapper()
        
    def give_roles(self, id: str, roles: List[Role]) -> UserAccount:
        user = self.__get_user.get_by_id(id)
        user_table = self._mapper.to_table(user)
        for role in roles:
            role_table = self.__role_mapper.to_table(role)
            UserRoleTableData.objects.create(employee=user_table, role=role_table)
        return self._mapper.to_model(user_table)
    
    def remove_roles(self, id: str, roles: List[Role]) -> UserAccount:
        user = self.__get_user.get_by_id(id)
        user_table = self._mapper.to_table(user)
        for role in roles:
            role_table = self.__role_mapper.to_table(role)
            UserRoleTableData.objects.get(employee=user_table, role=role_table).delete()
        return self._mapper.to_model(user_table)