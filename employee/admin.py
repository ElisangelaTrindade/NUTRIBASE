from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    ...
    def has_module_permission(self, request):
        return False
