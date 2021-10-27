from food_group.models import Food, FoodGroup
from django.core.management.base import BaseCommand
import csv
import os


class Command(BaseCommand):
    help = 'Create base groups'

    def handle(self, *args, **kwargs):
        path = os.path.join(os.path.abspath(os.path.dirname('manage.py')), 'tables')
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            group_name, group_calories = file.split('.')[0].split('_')
            new_food_group, group_created = FoodGroup.objects.get_or_create(group=group_name, calories=group_calories)
            with open(file_path,  encoding='utf-8-sig') as f:
                for row in csv.reader(f,quotechar="'"):
                    for i in range(len(row)):
                        if len(row[i].strip()) == 0:
                            row[i] = "0"
                    
                    new_food, food_created = Food.objects.get_or_create(food_group=new_food_group,
                    food_name=row[0], protein=float(row[1]), lipids=float(row[2]), cholesterol=float(row[3]),
                    carbohydrates=float(row[4]), dietary_fiber=float(row[5]), iron=float(row[6]), vitamin_c=float(row[7]),
                    calcium=float(row[8]), calories=float(row[9]), weight=float(row[10]))