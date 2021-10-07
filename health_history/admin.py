from django.contrib import admin
from health_history.models import FamilyHealthHistory, PatientHealthHistory



admin.site.register(FamilyHealthHistory)
admin.site.register(PatientHealthHistory)


