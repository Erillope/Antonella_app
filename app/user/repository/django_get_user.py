from src.user import GetUser, UserAccount, Role
from app.common.django_repository import DjangoGetModel, ModelNotFoundException
from .tables import UserAccountTableData, UserRoleTableData, UserTableMapper, RoleTableMapper
from typing import List

class DjangoGetUser(GetUser, DjangoGetModel[UserAccountTableData, UserAccount]):
    def __init__(self) -> None:
        super().__init__(UserAccountTableData, UserTableMapper())
        self.__role_mapper = RoleTableMapper()
        self.set_allowed_fields(['name', 'status', 'birthdate', 'created_date'])
        
    def get_by_account(self, account: str) -> UserAccount:
        if not self._table.objects.filter(account=account).exists():
            raise ModelNotFoundException.not_found(account)
        table = self._table.objects.get(account=account)
        return self._mapper.to_model(table)
    
    def get_roles(self, id: str) -> List[Role]:
        user = self.get_by_id(id)
        table = self._mapper.to_table(user)
        roles = UserRoleTableData.get_roles_from_user(table)
        return [self.__role_mapper.to_model(role) for role in roles]