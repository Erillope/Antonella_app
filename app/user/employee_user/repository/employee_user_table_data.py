from app.user.account.user_account_table_data import UserAccountTableData
from django.db import models

class EmployeeUserTableData(UserAccountTableData):
    user_account = models.OneToOneField(
        UserAccountTableData,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    
    class Meta:
        db_table = "employee_user"