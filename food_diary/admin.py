from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from food_diary.models import FoodDiary
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

 
class FoodDiaryAdmin(nested_admin.NestedModelAdmin):
  model = FoodDiary
  exclude = ('registered_by', )
  inlines = [
      MealAdmin,
  ]

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()


admin.site.register(FoodDiary, FoodDiaryAdmin)
