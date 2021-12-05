from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from diet_plan.custom_widgets import MealSelectWidget 
from food_diary.models import FoodDiary
from meal.models import Meal, MealFood
import nested_admin

class MealFoodAdmin(nested_admin.NestedStackedInline):
  model = MealFood
  def formfield_for_dbfield(self, db_field, **kwargs):
    if db_field.name == 'food':
        kwargs['widget'] = MealSelectWidget 
    return super(MealFoodAdmin, self).formfield_for_dbfield(db_field,**kwargs) 


class MealAdmin(nested_admin.NestedGenericTabularInline):
  model = Meal
  min_num= 1
  max_num= 3
  exclude = ('registered_by',  )
  inlines = [
      MealFoodAdmin,
  ]

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()

 
class FoodDiaryAdmin(nested_admin.NestedModelAdmin):
  model = FoodDiary
  min_num= 1
  max_num= 3
  exclude = ('registered_by', )
  inlines = [
      MealAdmin,
  ]
  search_fields = ['patient__first_name','patient__last_name','patient__cpf', ]
  class Media:
    js = (
      'js/calculate_calories.js',
    )

  def save_model(self, request, obj, form, change) :
    obj.registered_by_id = request.user.id
    obj.save()


admin.site.register(FoodDiary, FoodDiaryAdmin)
