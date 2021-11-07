from django.conf.urls import url
from django.contrib import admin
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
  exclude = ('registered_by',)
  inlines = [
      MealAdmin,
  ]
  search_fields = ['patient__first_name','patient__last_name','patient__cpf', ]

  def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()
  
  class Media:
    js = (
      'js/calculate_calories.js',
    )

admin.site.register(DietPlan, DietPlanAdmin)

