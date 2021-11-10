from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from diet_plan.models import DietPlan
from meal.models import Meal, MealFood
from .custom_widgets import MealSelectWidget 

import nested_admin

class MealFoodAdmin(nested_admin.NestedStackedInline):
  model = MealFood
  def formfield_for_dbfield(self, db_field, **kwargs):
    if db_field.name == 'food':
        kwargs['widget'] = MealSelectWidget 
    return super(MealFoodAdmin, self).formfield_for_dbfield(db_field,**kwargs) 


class MealAdmin(nested_admin.NestedGenericTabularInline):
  model = Meal
  exclude = ('registered_by', )
  min_num = 1
  can_delete= False
  inlines = [
      MealFoodAdmin,

  ]
  

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()

 
class DietPlanAdmin(nested_admin.NestedModelAdmin):
  model = DietPlan 
  inlines = [
      MealAdmin,
  ]
  search_fields = ['patient__first_name','patient__last_name','patient__cpf', ]
  readonly_fields = ('generate_pdf', )
  def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

  def get_fields(self, request, obj=None):
      if obj: #This is the case when obj is already created i.e. it's an edit
          return ('generate_pdf', 'patient', 'description', 'date_of_creation',)
      else:
          return ('patient', 'description', 'date_of_creation',)
  
  class Media:
    js = (
      'js/calculate_calories.js',
    )
  def generate_pdf(self, obj):
        return format_html(
            '<a class="button" href="/render/pdf/{}" target="_blank">' + _('Generate PDF') + '</a>',
            obj.pk
        )
  generate_pdf.short_description = _('Generate PDF')
  generate_pdf.allow_tags = True

admin.site.register(DietPlan, DietPlanAdmin)


    