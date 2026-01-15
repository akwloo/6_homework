from django.contrib import admin
from . models import User
from import_export.admin import ImportExportModelAdmin
from .resources import UserResource

class UserAdmin(ImportExportModelAdmin):
  list_display = ("firstName", "lastName", "maidenName", "age", "gender", "email", "phone", "username", "password", "birthDate", 
                  "bloodGroup", "height", "weight", "eyeColor", "role",)
  resource_class = UserResource

admin.site.register(User, UserAdmin)