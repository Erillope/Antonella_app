from src.user.account.data_providers import ExistsUser
from .employee_user_table_data import EmployeeUserTableData
from singleton_decorator import singleton

@singleton
class DjangoExistsEmployeeUser(ExistsUser):
    def exists_by_account(self, account: str) -> bool:
        return EmployeeUserTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return EmployeeUserTableData.objects.filter(id=id).exists()