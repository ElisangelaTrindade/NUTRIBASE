from django.test import TestCase
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from user.models import User 
from location.models import City, State
from patient.models import Patient
from food_diary.models import FoodDiary
import datetime

# Create your tests here.
class FoodDiaryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #registered by
        user = User.objects.create_user(username="Ana", email="ana@gmail.net", password= "password")
        user.is_superuser = True
        user.save()

        if City.objects.count() == 0:
            PopulateLocationCommand().populateDatabase()

        patient1= Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday="1990-04-17", email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code="000000")
        patient1.save()
        
        food_diary=FoodDiary.objects.create(patient=patient1, registered_by=user, description= "test",  date_of_consultation="2021-11-12" )
        food_diary.save()

    def test_food_diary(self):
        food_diary = FoodDiary.objects.first()
        self.assertEqual(food_diary.description,"test", "The field was registered correctly")
        self.assertEqual(food_diary.date_of_consultation, datetime.date(2021, 11, 12), "The date of consultation registered correctly")
        