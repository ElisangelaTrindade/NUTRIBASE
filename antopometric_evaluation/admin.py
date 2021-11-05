from django.contrib import admin
from antopometric_evaluation.models import AntopometricEvaluation

@admin.register(AntopometricEvaluation)
class AntopometricEvaluationAdmin(admin.ModelAdmin):
  model = AntopometricEvaluation
  exclude = ('registered_by',)
  search_fields = ['patient__first_name','patient__last_name','patient__cpf', ]

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()

 
