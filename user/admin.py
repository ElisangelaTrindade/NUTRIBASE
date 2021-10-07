from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User
from employee.models import Employee

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = True
    verbose_name_plural = 'employee'

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    inlines = (EmployeeInline,)

# Register your models here.



