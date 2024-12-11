from django.db import models

class RoleTableData(models.Model):
    role = models.CharField(max_length=250, blank=False, primary_key=True)
    created_date = models.DateField(auto_now_add=True, editable=False)
    
    class Meta:
        db_table = "role"