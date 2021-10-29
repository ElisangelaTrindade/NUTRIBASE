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

admin.site.register(ExerciseType, ExerciseTypeAdmin)
