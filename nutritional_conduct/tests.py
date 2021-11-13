from django.test import TestCase
from django.utils import timezone
from django.test import TestCase
from diet_plan.models import DietPlan
from food_group.models import Food, FoodGroup
from patient.models import Patient
from antopometric_evaluation.models import AntopometricEvaluation
from nutritional_conduct.models import NutritionalConduct
from user.models import User 
from location.models import City, State
from meal.models import Meal, MealFood
from food_group.models import FoodGroup
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from food_group.management.commands.populate_food import Command as PopulateFoodCommand
from django.contrib.contenttypes.models import ContentType
import datetime

# Create your tests here.
class NutricionalConductTest(TestCase):
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

        patient1=Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday=datetime.date(1990, 4, 17), email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code="000000", gender='F')
        AntopometricEvaluation.objects.create(patient=patient1, registered_by=user, weight=60.0, height= 1.75, arm_circumference=28, abdomen_circumference=80, wrist_circumference=14, date_of_consultation=datetime.date(2021, 11, 12), updated=datetime.date(2021, 11, 12))
        diet_plan=DietPlan.objects.create(patient=patient1, registered_by=user, description= "diet plan 1.500 calories", date_of_creation=datetime.date(2021, 11, 12))
        meal1=Meal.objects.create(type_meal= "Jantar", time_meal=timezone.now(), object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id, )
        MealFood.objects.create(food=Food.objects.first(), meal=meal1, weight= 140)

        
    def test_exercise_activity_factor(self):
        antopometric_evaluation = AntopometricEvaluation.objects.first()
        conduct = NutritionalConduct.objects.create(patient=antopometric_evaluation.patient, antopometric_evaluation=antopometric_evaluation, \
            diet_plan=DietPlan.objects.first(), exercise_type='L', date_of_consultation=datetime.date(2021, 11, 12))
        self.assertEqual(conduct.activity_factor(), 1.56)

        conduct.exercise_type='M'
        self.assertEqual(conduct.activity_factor(), 1.64)

        conduct.exercise_type='I'
        self.assertEqual(conduct.activity_factor(), 1.82)

        conduct.patient.gender='M'
        self.assertEqual(conduct.activity_factor(), 2.10)

        conduct.exercise_type='M'
        self.assertEqual(conduct.activity_factor(), 1.78)

        conduct.exercise_type='L'
        self.assertEqual(conduct.activity_factor(), 1.56)

        
    def test_essential_calorie_basal(self):
        antopometric_evaluation = AntopometricEvaluation.objects.first()
        antopometric_evaluation.patient.gender='M'
        conduct_cal_basal = NutritionalConduct.objects.create(patient=antopometric_evaluation.patient, antopometric_evaluation=antopometric_evaluation, \
            diet_plan=DietPlan.objects.first(), date_of_consultation=datetime.date(2021, 11, 12))
        self.assertEqual(conduct_cal_basal.essential_calorie_basal(), 1575.0)

    
    def test_conduct_bmi(self):
        antopometric_evaluation = AntopometricEvaluation.objects.first()
        test_conduct_bmi = NutritionalConduct.objects.create(patient=antopometric_evaluation.patient, antopometric_evaluation=antopometric_evaluation, \
            diet_plan=DietPlan.objects.first(), date_of_consultation=datetime.date(2021, 11, 12))
        self.assertEqual(test_conduct_bmi.calculate_bmi(), 19.59)






      