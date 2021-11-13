from django.test import TestCase
import datetime
from location.management.commands.populate_locations import Command as PopulateLocationCommand
from user.models import User 
from location.models import City, State
from patient.models import Patient
from clinic_evaluation.models import ClinicEvaluation, LabExam


# Create your tests here.
class ClinicEvaluationTest(TestCase):
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
        
        clinic_evaluation=ClinicEvaluation.objects.create(patient=patient1, registered_by=user, nails="strong", skin= "normal", bladder_habits="normal", bowel_habits="normal", additional_information="test", date_of_consultation="2021-11-12", updated="2021-11-12")
        clinic_evaluation.save()

    def test_clinic_evaluation(self):
        clinic_evaluation = ClinicEvaluation.objects.first()
        self.assertEqual(clinic_evaluation.nails, "strong", "The nails field was  registered correctly")
        self.assertEqual(clinic_evaluation.skin, "normal", "The skins field was registered correctly")
        self.assertEqual(clinic_evaluation.bladder_habits, "normal", "The bladder habits was registered correctly")
        self.assertEqual(clinic_evaluation.bowel_habits, "normal", "The bowel habits registered correctly")
        self.assertEqual(clinic_evaluation.date_of_consultation, datetime.date(2021, 11, 12), "The date of consultation registered correctly")
        self.assertEqual(clinic_evaluation.updated, datetime.date(2021, 11, 12), "This field registered correctly")
        self.assertEqual(clinic_evaluation.additional_information, "test", "This fiels was registered correctly")

    def test_lab_exam(self):
        lab_exam=LabExam.objects.create( name_exam ="exame de sangue", date_of_exam="2021-11-12", upload="test", exam_information= "exemplo glicemia=180", clinic_evaluation=ClinicEvaluation.objects.first() )
        lab_exam.save()
        lab_exam = LabExam.objects.first()
        self.assertEqual(lab_exam.name_exam, "exame de sangue", "The name was registered correctly")
        self.assertEqual(lab_exam.date_of_exam, datetime.date(2021, 11, 12), "The field date of exam registered correctly")
        self.assertEqual(lab_exam.upload, "test", "The field updated registered correctly")
        self.assertEqual(lab_exam.exam_information,"exemplo glicemia=180","This fild was registered correctly") 


        
