from django.contrib import admin

from .models import Employees


class EmployeeList(admin.ModelAdmin):
    list_display = ('emp_number', 'name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'name', 'city')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']



admin.site.register(Employees)
