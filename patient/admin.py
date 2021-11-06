from django.contrib import admin
from patient.models import Patient
from phone.models import Phone
from django.contrib.contenttypes.admin import GenericTabularInline

class PhoneAdmin(GenericTabularInline):
  model = Phone
  exclude = ('registered_by', )
  min_num = 2
  max_num = 2
  

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name','cpf', ]
    inlines = [PhoneAdmin]

admin.site.register(Patient, PatientAdmin)

