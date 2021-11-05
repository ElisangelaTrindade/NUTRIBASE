from django.contrib import admin

# Register your models here.
from patient.models import Patient


class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name','cpf', ]
admin.site.register(Patient, PatientAdmin)

