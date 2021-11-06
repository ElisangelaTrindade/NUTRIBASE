from django.contrib import admin
from exercise.models import  ExerciseType
from patient.models import Patient


class ExerciseTypeAdmin(admin.ModelAdmin):
    model = ExerciseType

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

admin.site.register(ExerciseType, ExerciseTypeAdmin)




