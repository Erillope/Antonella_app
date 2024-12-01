from src.user.account.data_providers import GetUser, ExistsUser, SaveUser
from src.user.employee_user.data_providers import (EmployeeUserRepositoryConfiguration, GetRole,
                                                   SaveRole, DeleteRole)
from ..repository import (DjangoGetEmployeeUser, DjangoExistsEmployeeUser, DjangoSaveEmployee,
                          DjangoGetRole, DjangoSaveRole, DjangoDeleteRole)
from singleton_decorator import singleton

@singleton
class DjangoEmployeeUserRepositoryConfiguration(EmployeeUserRepositoryConfiguration):
    def construct_get_user(self) -> GetUser:
        return DjangoGetEmployeeUser(
            exists_employee_user = self.construct_exists_user()
        )
    
    def construct_save_user(self) -> SaveUser:
        return DjangoSaveEmployee()
    
    def construct_exists_user(self) -> ExistsUser:
        return DjangoExistsEmployeeUser()
    
    def construct_get_role(self) -> GetRole:
        return DjangoGetRole()
    
    def construct_save_role(self) -> SaveRole:
        return DjangoSaveRole()
    
    def construct_delete_role(self) -> DeleteRole:
        return DjangoDeleteRole()