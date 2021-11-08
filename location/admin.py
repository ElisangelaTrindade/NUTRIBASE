from django.contrib import admin
class LocationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False