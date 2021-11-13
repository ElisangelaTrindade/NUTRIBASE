from django.test import TestCase
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from user.models import User 
from location.models import City, State
from patient.models import Patient
from antopometric_evaluation.models import AntopometricEvaluation

class AntopometricEvaluationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #registered by
        user = User.objects.create_user(username="Ana", email="ana@gmail.net", password= "password")
        user.is_superuser = True
        

        if City.objects.count() == 0:
            PopulateLocationCommand().populateDatabase()

        patient1= Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday="1990-04-17", email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code="000000")
        patient1.save()
        
        antopometric_evaluation=AntopometricEvaluation.objects.create(patient=patient1, registered_by=user, weight=60.0, height= 1.75, arm_circumference=28, abdomen_circumference=80, wrist_circumference=14, date_of_consultation="2021-11-12", updated="2021-11-12")
        antopometric_evaluation.save()

    def test_antopometric_evaluation(self):
        antopometric_evaluation = AntopometricEvaluation.objects.first()
        self.assertGreater(antopometric_evaluation.weight,0, "The weight must be greater than 0")
        self.assertGreater(antopometric_evaluation.height,0, "The height must be greater than 0")
        self.assertGreater(antopometric_evaluation.arm_circumference,0, "The arm circumference must be greater than 0")
        self.assertGreater(antopometric_evaluation.abdomen_circumference,0, "The abdomen circumference must be greater than 0")
        self.assertGreater(antopometric_evaluation.wrist_circumference,0, "The abdomen circumference must be greater than 0")
    