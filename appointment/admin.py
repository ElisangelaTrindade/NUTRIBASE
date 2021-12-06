from django.contrib import admin
from appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    search_fields = ['patient__first_name','patient__last_name','patient__cpf']

admin.site.register(Appointment, AppointmentAdmin)
