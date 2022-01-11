from django.db import models
from django.utils.translation import deactivate

# Create your models here.

class LeaveRequest(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.BooleanField(default=False)
    