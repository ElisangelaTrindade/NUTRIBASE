from django.conf.urls import url
from django.contrib import admin
from diet_plan.models import DietPlan
from meal.models import Meal, MealFood
from .views import Pdf
import nested_admin

class MealFoodAdmin(nested_admin.NestedStackedInline):
  model = MealFood


class MealAdmin(nested_admin.NestedGenericTabularInline):
  model = Meal
  exclude = ('registered_by', )
  max_num = 6
  min_num = 3
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
  

admin.site.register(DietPlan, DietPlanAdmin)

