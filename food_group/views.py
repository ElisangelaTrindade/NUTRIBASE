from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class CaloriesQuery(View):
    def get(self, request, food_id, weight_value):
        return HttpResponse("test");
