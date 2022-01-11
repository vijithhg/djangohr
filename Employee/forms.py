from django.forms import ModelForm, fields
from .models import *

class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date','end_date','reason']