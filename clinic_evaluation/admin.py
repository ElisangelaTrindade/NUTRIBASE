from django.contrib import admin
from clinic_evaluation.models import ClinicEvaluation, GastrointestinalTractSymptoms, LabExam


class GastrointestinalTractSymptomsInline(admin.StackedInline):
    model = GastrointestinalTractSymptoms
    verbose_name_plural = 'gastrointestinal_tract_symptoms'
    fieldsets = (('', {
            'fields': ('dysphagia','pain', 'reflux', 'heart_burn', 'constipation', 'nausea', 'diarrhea', 'others',)
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class LabExamInline(admin.StackedInline):
    model = LabExam
    verbose_name_plural = 'lab_exam'
    fieldsets = (('', {
            'fields': ('name_exam', 'date_of_exam','upload','exam_information',)
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class ClinicEvaluationAdmin(admin.ModelAdmin):
    model = ClinicEvaluation
    inlines = (GastrointestinalTractSymptomsInline, LabExamInline,)
    exclude = ('registered_by', )

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

admin.site.register(ClinicEvaluation, ClinicEvaluationAdmin)



