from django.contrib import admin
from exercise.models import  ExerciseType, Exercise



class ExerciseTypeAdmin(admin.ModelAdmin):
    model = ExerciseType

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

    def has_module_permission(self, request):
        return False

admin.site.register(ExerciseType, ExerciseTypeAdmin)



    

