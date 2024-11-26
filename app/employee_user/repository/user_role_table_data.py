from django.db import models
from .employee_user_table_data import EmployeeUserTableData
from .role_table_data import RoleTableData
from typing import Set

class UserRoleTableData(models.Model):
    employee = models.ForeignKey(EmployeeUserTableData, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleTableData, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, editable=False)
    
    @staticmethod
    def get_roles_from_employee(employee_table: EmployeeUserTableData) -> Set[RoleTableData]:
        user_role_tables = UserRoleTableData.objects.filter(employee=employee_table)
        return set([table.role for table in user_role_tables])

    class Meta:
        db_table = "user_role"
        constraints = [
            models.UniqueConstraint(fields=['employee', 'role'], name='unique_employee_role')
        ]