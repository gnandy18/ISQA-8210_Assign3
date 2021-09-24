from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('emp_number', 'name', 'address', 'city', 'state', 'zipcode', 'cell_phone',)
