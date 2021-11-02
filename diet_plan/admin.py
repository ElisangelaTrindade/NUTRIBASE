from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from diet_plan.models import DietPlan
from meal.models import Meal, MealFood
import nested_admin

class MealFoodAdmin(nested_admin.NestedStackedInline):
  model = MealFood


class MealAdmin(nested_admin.NestedGenericTabularInline):
  model = Meal
  exclude = ('registered_by', )
  inlines = [
      MealFoodAdmin,
  ]

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()

 
class DietPlanAdmin(nested_admin.NestedModelAdmin):
  model = DietPlan 
  exclude = ('registered_by', )
  inlines = [
      MealAdmin,
  ]

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()

admin.site.register(DietPlan, DietPlanAdmin)



