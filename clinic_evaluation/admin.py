from django.contrib import admin
from clinic_evaluation.models import ClinicEvaluation, GastrointestinalTractSymptoms, LabExam

admin.site.register(ClinicEvaluation)
admin.site.register(GastrointestinalTractSymptoms)
admin.site.register(LabExam)