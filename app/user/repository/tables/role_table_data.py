from django.db import models

class RoleTableData(models.Model):
    id = models.UUIDField(primary_key=True)
    role = models.CharField(max_length=250, blank=False)
    created_date = models.DateField(auto_now_add=True, editable=False)
    
    class Meta:
        db_table = "role"