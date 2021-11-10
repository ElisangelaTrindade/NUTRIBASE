from django.contrib import admin

from nutritional_conduct.models import NutritionalConduct

#ToDo delete this model later
@admin.register(NutritionalConduct)
class NutritionalConductAdmin(admin.ModelAdmin):
  model = NutritionalConduct
  exclude = ('registered_by',)
  readonly_fields = ('stringify_calory_need', 'stringify_bmi','stringify_cir_abdominal' )

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()