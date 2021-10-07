from django.contrib import admin

# Register your models here.
from location.models import State, City



admin.site.register(State)
admin.site.register(City)