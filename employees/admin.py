import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Employees


class EmployeeListExportCsvMixin:
    def export_as_csv(self, request, queryset):
        emp_list = Employees.objects.all().only("name", "address", "emp_number",
                                                "city", "state", "zipcode", "cell_phone")
        formatted_field_names = ['Name', 'Address', 'EmpID', 'City', 'State',
                                 'Zipcode', 'Phone']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=employeelist.csv'
        writer = csv.writer(response)
        writer.writerow(formatted_field_names)
        for emp_list in queryset:
            writer.writerow([emp_list.name,
                             emp_list.address,
                             emp_list.emp_number, emp_list.city,
                             emp_list.state, emp_list.zipcode, emp_list.cell_phone])

        return response

    export_as_csv.short_description = "Generate Employee List"


class EmployeeList(admin.ModelAdmin, EmployeeListExportCsvMixin):
    list_display = ('emp_number', 'name', 'city', 'cell_phone')
    list_filter = ('emp_number', 'name', 'city')
    search_fields = ('emp_number', 'name')
    ordering = ['emp_number']
    actions = ["export_as_csv"]


admin.site.register(Employees, EmployeeList)
