from django.test import TestCase
from django.utils import timezone
from django.test import TestCase
from diet_plan.models import DietPlan
from food_group.models import Food, FoodGroup
from patient.models import Patient
from user.models import User 
from location.models import City, State
from meal.models import Meal, MealFood
from food_group.models import FoodGroup
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from food_group.management.commands.populate_food import Command as PopulateFoodCommand
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

# Create your tests here.
class MealFoodTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        if City.objects.count() == 0:
            PopulateLocationCommand().populateDatabase()

        if FoodGroup.objects.count() == 0:
            PopulateFoodCommand().populateDatabase()

        user = User.objects.create_user(username="Ana", email="ana@gmail.net", password= "password", is_superuser = True)
        patient1 = Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday="1990-04-17", email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code="000000")
        diet_plan = DietPlan.objects.create(patient=patient1, registered_by=user, description="diet plan 1.500 calories", date_of_creation="2021-11-12")        
        Meal.objects.create(type_meal="Jantar", time_meal=timezone.now(), object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id)
        
    def test_meal_food(self):
        meal_food = MealFood.objects.create(food=Food.objects.first(), meal=Meal.objects.first(), weight=140)
        self.assertGreater(meal_food.weight,0 ,"The weight must be greater than 0")
        self.assertGreater(meal_food.food.food_group.calories, 0, "The calories must be greater than 0")

    def test_meal_food_must_have(self):
        meal_food = MealFood.objects.create(food=Food.objects.first(), meal=Meal.objects.first(), weight=0)
        with self.assertRaises(ValidationError):
           meal_food.full_clean()

       