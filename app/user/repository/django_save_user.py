from src.user import SaveUser, UserAccount
from .tables import UserAccountTableData, UserTableMapper, UserRoleTableData, RoleTableMapper
from typing import List

class DjangoSaveUser(SaveUser):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = UserTableMapper()
        self.__role_mapper = RoleTableMapper()

    def save(self, user: UserAccount) -> UserAccount:
        user_table = self.__mapper.to_table(user)
        user_table.save()
        self.__save_roles(user, user_table)
        roles = UserRoleTableData.get_roles_from_user(user_table)
        return self.__mapper.to_user(user_table, roles)
    
    def __save_roles(self, user: UserAccount, user_table: UserAccountTableData) -> None:
        user_role_tables = UserRoleTableData.objects.filter(employee=user_table)
        if self.__table_have_more_role_than_user(user, user_role_tables):
            self.__take_roles(user_role_tables, user)
        if self.__user_have_more_role_than_table(user, user_role_tables):
            self.__give_role(user_table, user)
            
    def __table_have_more_role_than_user(self, user: UserAccount,
                                             user_role_tables: List[UserRoleTableData]) -> bool:
        return len(user_role_tables) > len(user.get_roles())
    
    def __user_have_more_role_than_table(self, user: UserAccount,
                                             user_role_tables: List[UserRoleTableData]) -> bool:
        return len(user_role_tables) < len(user.get_roles())
    
    def __take_roles(self, user_role_tables: List[UserRoleTableData], user: UserAccount) -> None:
        for user_role in user_role_tables:
            role = self.__role_mapper.to_role(user_role.role)
            if not user.have_role(role):
                user_role.delete()
    
    def __give_role(self, user_table: UserAccountTableData, user: UserAccount) -> None:
        for role in user.get_roles():
            role_table = self.__role_mapper.to_table(role)
            if not UserRoleTableData.objects.filter(employee=user_table, role=role_table).exists():
                UserRoleTableData.objects.create(employee=user_table, role=role_table)