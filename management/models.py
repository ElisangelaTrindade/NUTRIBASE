from django.db import models
from cpffield import cpffield
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # igual modelo padrao com um campo bio a mais
  bio= models.TextField(blank=True)

class State(models.Model):
  name_state = models.CharField(max_length=50,db_column='name_state')
  acrm_state = models.CharField(max_length=3,db_column='acrm_state')

  class Meta:
    db_table ='state'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.acrm_state

class City(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  name_city = models.CharField(max_length=50, db_column='name_city')

  class Meta:
    db_table ='city'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.name_state

class FamilyHealthHistory(models.Model):
  obesity = models.CharField(max_length=100, db_column='obesity ')
  cardiovascular_disease = models.CharField(max_length=100, db_column='cardiovascular_disease')
  hypertension = models.CharField(max_length=100, db_column='hypertension')
  cancer = models.CharField(max_length=100, db_column='cancer')
  diabetes = models.CharField(max_length=100, db_column='diabetes')
  dyslipidemia = models.CharField(max_length=100, db_column='dyslipidemia')

  class Meta:
    db_table ='family_health_history' # preciso de def?

class PatientHealthHistory(models.Model):
  obesity = models.CharField(max_length=100, db_column='obesity')
  cardiovascular_disease = models.CharField(max_length=100, db_column='cardiovascular_disease')
  hypertension = models.CharField(max_length=100, db_column='hypertension')
  cancer = models.CharField(max_length=100, db_column='cancer')
  diabetes = models.CharField(max_length=100, db_column='diabetes')
  dyslipidemia = models.CharField(max_length=100, db_column='dyslipidemia')
  others = models.CharField(max_length=100, db_column='others')

  class Meta:
    db_table ='patient_health_history' # preciso de def?

class Exercise(models.Model):
    type = models.CharField(max_length=255, help_text='type')
    frequency = models.CharField(max_length=255, help_text='frequency')
    def __str__(self):
        return self.type+ self.patient.frequency

class Patient(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  family_health_history = models.ForeignKey(FamilyHealthHistory, on_delete=models.CASCADE)
  patient_health_history = models.ForeignKey(PatientHealthHistory, on_delete=models.CASCADE)
  exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE)
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50)
  city = models.OneToOneField(City, on_delete=models.CASCADE)
  zip_code = models.CharField(max_length=9,default = '')

  GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
    )
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

  class Meta:
    db_table ='patient'
    def __str__(self):
      return self.user.first_name + ' ' + self.user.last_name

class Employee(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  hire_date = models.DateField(db_column='hire_date')
  type = models.CharField(max_length=50,db_column='type')
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50, db_column='street')
  city = models.OneToOneField(City, on_delete=models.CASCADE)
  zip_code = models.CharField(max_length=9,default = '')
    
  class Meta:
    db_table ='employee'
    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Phone(models.Model):
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE) #ta errado?
    phone_number = models.CharField(max_length=12)
    description = models.CharField(max_length=25)
    
    def __str__(self):
        return self.phone_number

class FoodDiary(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.CharField(max_length=255,db_column='description')
  date_of_consultation=models.DateField()
  gram_weigh=models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')

  class Meta:
    db_table ='food_diary' # preciso de def?

class DietPlan(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.CharField(max_length=255,db_column='description')
  date_of_creation=models.DateField()
  amount_of_calories=models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')
  gram_weigh=models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')
  class Meta:
    db_table ='diet_plan' # preciso de def?
  
class Meal(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  food_diary = models.ForeignKey(FoodDiary, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  type_meal = models.CharField(max_length=50,db_column='type_meal')
  time_meal = models.DateTimeField(auto_now_add=True,db_column='time_meal')

  class Meta:
    db_table ='meal'

    def __str__(self):
      return self.name_meal

    def __date__(self):
      return self.time_meal

class FoodGroup(models.Model): 
  name_group = models.CharField(max_length=150,db_column='name_group')
  gram_weight = models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')
  calorie = models.PositiveIntegerField(default=0)

  class Meta:
    db_table ='food_group' # parei de por o def aqu

class Food(models.Model):
  food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
  diet_plan = models.OneToOneField(DietPlan, on_delete=models.CASCADE)
  food_name=models.CharField(max_length=50, db_column='food_name')
  gram_weigh=models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')
  
  class Meta:
    db_table ='food' # preciso de def?

class FoodConsumption(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  soft_drink = models.CharField(max_length=100, db_column='soft_drink')
  candy = models.CharField(max_length=100, db_column='candy')
  deep_fried = models.CharField(max_length=100, db_column='deep_fried')
  fast_food= models.CharField(max_length=100, db_column='fast_food')
  processed_food = models.CharField(max_length=100, db_column='processed_food')
  canned_food = models.CharField(max_length=100, db_column='canned')
  fruits = models.CharField(max_length=100, db_column='fruits')
  vegetables = models.CharField(max_length=100, db_column='vegetables')
  others = models.CharField(max_length=100, db_column='others')
  class Meta:
    db_table ='food_consumption' # preciso de def?

class FoodIntolerance(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  intolerance_description= models.CharField(max_length=255, db_column='description')
  class Meta:
    db_table ='food_intolerance' # preciso de def?

class FoodPreferences(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_description= models.CharField(max_length=100, db_column='description')
  class Meta:
    db_table ='food_preferences' # preciso de def?

class NutritionalInformation(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE)
  food_preferences = models.OneToOneField(User, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)#
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)#
  additional_information= models.CharField(max_length=255, db_column='description')
  class Meta:
    db_table ='nutricional_information' # preciso de def?

class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=6, decimal_places=2, help_text='weight') 
  height = models.CharField(max_length=4,)
  BMI = models.DecimalField(max_digits=4, decimal_places=2, help_text='bmi')
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, help_text='arm_circumference') 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, help_text='abdomen_circumference') 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, help_text='wrist_circumference')
  additional_information= models.CharField(max_length=100, db_column='additional_information=')
  class Meta:
    db_table ='antopometric_evaluation' # preciso de def?


class Lab_Exam (models.Model): # como fazer upload?
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  name_exam =models.CharField(max_length=100, db_column='description')
  lab_reference_values= models.DecimalField(max_digits=6, decimal_places=2, help_text='lab_reference_value') 
  lab_value_found= models.DecimalField(max_digits=6, decimal_places=2, help_text='ab_value_found') 
  additional_information= models.CharField(max_length=100, db_column='dditional_information')
  class Meta:
    db_table ='lab_exam' # preciso de def?        


class ClinicEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  nails= models.CharField(max_length=100, db_column='nails')
  skin = models.CharField(max_length=100, db_column='skin')
  bladder_habits = models.CharField(max_length=100, db_column='bladder_habits')
  bowel_habits = models.CharField(max_length=100, db_column='bowel_habits') 
  additional_information= models.CharField(max_length=100, db_column='additional_information=')
  class Meta:
    db_table ='clinic_evaluation' # preciso de def?