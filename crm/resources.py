from import_export import resources
from .models import Employee

class EmployeeResource(resources.ModelResource):

    #def before_import(self, queryset, **kwargs):
        #Employee.objects.all().delete()
        #super().before_import(queryset, **kwargs)

    def before_import_row(self, row, **kwargs):
        row["first_name"] = f"{str(row['first_name']).strip():.{10}}"
        row["last_name"] = f"{str(row['last_name']).strip():.{10}}"
        row["age"] = f"{row['age']:.{5}}"
        row["monthly_salary"] = f"{float(row['monthly_salary']):.{10}}"
        row["join_date"] = f"{str(row['join_date']).strip():.{15}}"
        super().before_import_row(row, **kwargs)

    #def after_export(self, queryset, data, **kwargs):
        #Employee.objects.all().delete()
        #super().after_export(queryset, data, **kwargs)

    class Meta:
        model = Employee
        widgets = {'join_date': {'format': '%Y-%m-%d'}}
