from django.contrib import admin
from patient.models import Patient
from phone.models import Phone
from django.contrib.contenttypes.admin import GenericTabularInline
from exercise.models import Exercise

class ExerciseAdmin(admin.StackedInline):
  model = Exercise
  min_num = 1
  max_num = 1
  

class PhoneAdmin(GenericTabularInline):
  model = Phone
  exclude = ('registered_by', )
  min_num = 2
  max_num = 2


class PatientAdmin(admin.ModelAdmin):
  search_fields = ['first_name','last_name','cpf', ]
  exclude = ('registered_by', )
  inlines = [PhoneAdmin, ExerciseAdmin]

  def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()


admin.site.register(Patient, PatientAdmin)


