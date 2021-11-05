from django.contrib import admin

# Register your models here.
from food_group.models import FoodGroup,Food


class FoodAdmin(admin.ModelAdmin):
    model = Food
    search_fields = ['food_name','food_group__group', ]

admin.site.register(Food, FoodAdmin)

