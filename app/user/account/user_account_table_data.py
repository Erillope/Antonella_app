from src.user.account import AccountStatus
from django.db import models

class UserAccountTableData(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    account = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=250, blank=False)
    status = models.CharField(max_length=25, choices=[(s.name, s.name) for s in AccountStatus])
    joined_date = models.DateField(auto_now_add=True, editable=False)
    
    class Meta:
        db_table = "user_account"