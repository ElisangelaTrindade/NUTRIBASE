from django.contrib import admin
from exercise.models import Exercise, ExerciseType

# Register your models here.
admin.site.register(Exercise)
admin.site.register(ExerciseType)