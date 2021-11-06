from django.contrib import admin
from django.contrib.admin.decorators import display
from django.contrib.auth import admin as auth_admin

from .models import User
from employee.models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = True
    verbose_name_plural = 'employee'
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
    inlines = (EmployeeInline,)
    search_fields = ['first_name','last_name','cpf', ]




