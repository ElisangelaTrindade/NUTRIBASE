from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User
from phone.models import Phone
from employee.models import Employee


class PhoneAdmin(GenericTabularInline):
  model = Phone
  exclude = ('registered_by', )
  min_num = 0
  
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = True
    verbose_name_plural = 'employee'
    exclude = ('registered_by',)
    fk_name = 'user'
    max_num = 1
    min_num = 1
    can_delete= False

def label_from_instance(self):
    return self.employee
  
def __str__(self):
    return self.employee


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    inlines = (EmployeeInline, PhoneAdmin)
    search_fields = ['first_name','last_name','cpf', ]




