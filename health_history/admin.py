from django.contrib import admin
from health_history.models import FamilyHealthHistory, PatientHealthHistory

class FamilyHealthHistoryInline(admin.StackedInline):
    model = FamilyHealthHistory
    verbose_name_plural='family_health_history'
    fieldsets = (('', {
        'fields': ('obesity', 'cardiovascular_disease','hypertension', 'cancer', 'diabetes', 'dyslipidemia', 'others', )
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class PatientHealthHistoryAdmin(admin.ModelAdmin):
    model = PatientHealthHistory
    inlines = (FamilyHealthHistoryInline,)

admin.site.register(PatientHealthHistory, PatientHealthHistoryAdmin )
