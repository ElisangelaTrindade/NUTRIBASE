from django.contrib import admin
from exercise.models import Exercise, ExerciseType

class ExerciseInline(admin.StackedInline):
    model = Exercise
    verbose_name_plural='exercise'
    fieldsets = (('', {
        'fields': ('exercise_type', 'patient', 'frequency')
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class ExerciseTypeAdmin(admin.ModelAdmin):
    model = ExerciseType
    inlines = (ExerciseInline,)
    exclude = ('registered_by', )
    search_fields = ['patient__first_name','patient__last_name','patient__cpf', ]

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

admin.site.register(ExerciseType, ExerciseTypeAdmin)




