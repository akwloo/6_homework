from django.contrib import admin
from . models import Employee
from import_export.admin import ImportExportModelAdmin
from .resources import EmployeeResource

class EmployeeAdmin(ImportExportModelAdmin):
  list_display = ("first_name", "last_name", "age", "monthly_salary", "join_date",)
  resource_class = EmployeeResource

admin.site.register(Employee, EmployeeAdmin)