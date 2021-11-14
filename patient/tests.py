from django.test import TestCase
from patient.models import Patient
from cpf_field.models import CPFField
from user.models import User
from location.models import City, State
from location.management.commands.populate_locations import Command as PopulateCommand


class PatientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        if City.objects.count() == 0:
            PopulateCommand().populateDatabase()
        
        user = User.objects.create_user(username='Ana', email='ana@gmail.net', password= 'password', is_superuser=True)
        Patient.objects.create(first_name="Cris", last_name="Silva",registered_by=user, cpf="06768725815",  birthday="1990-04-17", email= "teste@test@gmail.com", street= "Rua das flores 123", city=City.objects.first(), state=State.objects.first(), zip_code='000000', gender="F" )
       
    def test_patient_created(self):
        patient = Patient.objects.get(first_name="Cris")
        self.assertEqual(patient.first_name, "Cris", "The first name registered correctly")
        self.assertEqual(patient.last_name, "Silva", "The surname was registered correctly")
        
    def cpf_validation(self):
        field = CPFField()
        self.assertIsNone(field.validate("06768725815"))
        self.assertIsNone(field.validate("067.687.258-15"))
        self.assertIsNone(field.validate("067-687-258.15"))
        self.assertEqual("CPF must 11 characters", field.validate("0676872581"))
        self.assertEqual("CPF must 11 characters", field.validate("067687258155"))
        self.assertEqual("Invalid CPF", field.validate("067.687.258-00"))
  