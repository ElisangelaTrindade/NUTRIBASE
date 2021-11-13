from django.test import TestCase
from food_group.models import FoodGroup,Food
from django.core.exceptions import ValidationError
from food_group.management.commands.populate_food import Command as PopulateFoodCommand



class FoodGroupTest(TestCase):
    @classmethod
    def setUpTestData(cls):
    
        if FoodGroup.objects.count() == 0:
            PopulateFoodCommand().populateDatabase()
        
    def test_group_food_must_have(self):
        food_group1=FoodGroup.objects.create(group="Frutas", calories=0)
        with self.assertRaises(ValidationError):
            food_group1.full_clean()

    def test__food(self):
        food=Food.objects.create(food_group=FoodGroup.objects.first(), food_name="name", calories=0, weight=0)
        with self.assertRaises(ValidationError):
            food.full_clean()



            

