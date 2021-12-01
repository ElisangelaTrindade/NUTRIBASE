from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.models import ContentType
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

    def save_formset(self, request, form, formset, change):
        for f in formset.forms:
            obj = f.instance 
            if hasattr(obj, 'registered_by_id'):
                obj.registered_by_id = request.user.id
            if hasattr(obj, 'content_type_id'):
                obj.content_type_id = ContentType.objects.get_for_model(Phone).id
            if hasattr(obj, 'object_id'):
                obj.object_id = form.instance.id

            obj.save()

        formset.save()
    



