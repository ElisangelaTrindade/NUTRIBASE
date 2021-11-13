from django.utils import timezone
from django.test import TestCase
from diet_plan.models import DietPlan
from food_group.models import Food, FoodGroup
from patient.models import Patient
from antopometric_evaluation.models import AntopometricEvaluation
from user.models import User 
from location.models import City, State
from meal.models import Meal, MealFood
from food_group.models import FoodGroup
from clinic_evaluation.models import ClinicEvaluation
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from food_group.management.commands.populate_food import Command as PopulateFoodCommand
from django.contrib.contenttypes.models import ContentType

class DietPlanTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #registered by
        user = User.objects.create_user(username="Ana", email="ana@gmail.net", password= "password")
        user.is_superuser = True
        user.save()

        if City.objects.count() == 0:
            PopulateLocationCommand().populateDatabase()
        
        if FoodGroup.objects.count() == 0:
            PopulateFoodCommand().populateDatabase()

        patient1= Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday="1990-04-17", email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code="000000")
        patient1.save()
        AntopometricEvaluation.objects.create(patient=patient1, registered_by=user, weight=60.0, height= 1.75, arm_circumference=28, abdomen_circumference=80, wrist_circumference=14, date_of_consultation="2021-11-12", updated="2021-11-12")
        ClinicEvaluation.objects.create(patient=patient1, registered_by=user, nails="strong", skin= "normal", bladder_habits="normal", bowel_habits="normal", additional_information="test", date_of_consultation="2021-11-12", updated="2021-11-12")
        
        diet_plan = DietPlan.objects.create(patient=patient1, registered_by=user, description= "diet plan 1.500 calories", date_of_creation="2021-11-12")
        diet_plan.save()
        
        meal1=Meal.objects.create(type_meal= "Jantar", time_meal=timezone.now(), object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id)
        meal1.save()
        MealFood.objects.create(food=Food.objects.first(), meal=Meal.objects.first(), weight= 140)

        
    def test_diet_plan(self):
        diet_plan = DietPlan.objects.first()
        calories = diet_plan.calculate_total_of_calories()
        print (calories)
        self.assertEqual(calories, 560)
     



  