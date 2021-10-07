from django.contrib import admin

# Register your models here.
from food_group.models import FoodGroup,Food


admin.site.register(FoodGroup)
admin.site.register(Food)