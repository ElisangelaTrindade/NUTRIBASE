from django.contrib import admin

class PhoneAdmin(admin.ModelAdmin):
    ...
    def has_module_permission(self, request):
        return False
