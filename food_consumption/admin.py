from django.contrib import admin

# Register your models here.
from food_consumption.models import FoodConsumption,FoodIntolerance,FoodPreferences

# Register your models here.
admin.site.register(FoodConsumption)
admin.site.register(FoodIntolerance)
admin.site.register(FoodPreferences)