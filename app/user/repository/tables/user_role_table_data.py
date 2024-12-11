from django.db import models
from .user_account_table_data import UserAccountTableData
from .role_table_data import RoleTableData
from typing import List

class UserRoleTableData(models.Model):
    employee = models.ForeignKey(UserAccountTableData, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleTableData, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, editable=False)
    
    @classmethod
    def get_roles_from_user(cls, user_table: UserAccountTableData) -> List[RoleTableData]:
        user_role_tables = cls.objects.filter(employee=user_table)
        return [table.role for table in user_role_tables]

    class Meta:
        db_table = "user_role"
        constraints = [
            models.UniqueConstraint(fields=['employee', 'role'], name='unique_employee_role')
        ]