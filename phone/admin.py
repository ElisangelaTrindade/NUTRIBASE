from django.contrib import admin

class PhoneAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()
        
    def has_module_permission(self, request):
        return False
