from import_export import resources
from .models import User

class UserResource(resources.ModelResource):

    #def before_import(self, queryset, **kwargs):
        #User.objects.all().delete()
        #super().before_import(queryset, **kwargs)

    def before_import_row(self, row, **kwargs):
        row["firstName"] = f"{str(row['firstName']).strip():.{10}}"
        row["lastName"] = f"{str(row['lastName']).strip():.{10}}"
        row["maidenName"] = f"{str(row['maidenName']).strip():.{10}}"
        row["age"] = f"{float(row['age']):.{5}}"
        row["gender"] = f"{str(row['gender']).strip():.{10}}"
        row["email"] = f"{str(row['email']).strip():.{50}}"
        row["phone"] = f"{str(row['phone']).strip():.{20}}"
        row["username"] = f"{str(row['username']).strip():.{10}}"
        row["password"] = f"{str(row['password']).strip():.{10}}"
        row["birthDate"] = f"{str(row['birthDate']).strip():.{15}}"
        row["bloodGroup"] = f"{str(row['bloodGroup']).strip():.{5}}"
        row["height"] = f"{float(row['height']):.{8}}"
        row["weight"] = f"{float(row['weight']):.{8}}"
        row["eyeColor"] = f"{str(row['eyeColor']).strip():.{10}}"
        row["role"] = f"{str(row['role']).strip():.{10}}"
        super().before_import_row(row, **kwargs)

    #def after_export(self, queryset, data, **kwargs):
        #User.objects.all().delete()
        #super().after_export(queryset, data, **kwargs)

    class Meta:
        model = User
        widgets = {'birthDate': {'format': '%Y-%m-%d'}}
