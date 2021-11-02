from django.contrib import admin

# Register your models here.
from food_consumption.models import FoodConsumption,FoodIntolerance,FoodPreferences

class FoodIntoleranceInline(admin.StackedInline):
    model = FoodIntolerance
    verbose_name_plural='food_intolerance'
    fieldsets = (('', {
        'fields': ('intolerance_description',)
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class FoodPreferencesInline(admin.StackedInline):
    model = FoodPreferences
    verbose_name_plural='food_preferences'
    fieldsets = (('', {
        'fields': ('description',)
    }),)
    max_num = 1
    min_num = 1
    can_delete= False

class FoodConsumptionAdmin(admin.ModelAdmin):
    model = FoodConsumption
    inlines = (FoodIntoleranceInline, FoodPreferencesInline,)
    exclude = ('registered_by', )

    def save_model(self, request, obj, form, change) :
        obj.registered_by_id = request.user.id
        obj.save()

admin.site.register(FoodConsumption, FoodConsumptionAdmin)





