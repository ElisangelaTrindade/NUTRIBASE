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

class Patient(models.Model):
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  family_health_history = models.ForeignKey(FamilyHealthHistory, on_delete=models.CASCADE)
  patient_health_history = models.ForeignKey(PatientHealthHistory, on_delete=models.CASCADE)
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
    def __unicode__(self):
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

# irei por telefones de contato aqui mesmo?
# tenho que atualizar as tabelas?

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
  food_name=models.CharField(max_length=100, db_column='food_name')
  gram_weigh=models.DecimalField(max_digits=8, decimal_places=1, help_text='gram_weight')
  
  class Meta:
    db_table ='food' # preciso de def?

class FoodConsumption(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  soft_drink = models.CharField(max_length=100, db_column='soft_drink')
  candy = models.CharField(max_length=100, db_column='candy')
  deep_fried = models.CharField(max_length=100, db_column='deep_fried')
  fast_food= models.CharField(max_length=100, db_column='fast_food')
  #embutido? = models.CharField(max_length=100, db_column='')
  canned = models.CharField(max_length=100, db_column='canned')
  fruits = models.CharField(max_length=100, db_column='fruits')
  vegetables = models.CharField(max_length=100, db_column='vegetables')
  others = models.CharField(max_length=100, db_column='others')
  class Meta:
    db_table ='food_consumption' # preciso de def?

class FoodIntolerance(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.CharField(max_length=100, db_column='description')
  class Meta:
    db_table ='food_intolerance' # preciso de def?

class PreferenciaAlimentar(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  
  description= models.CharField(max_length=100, db_column='description')
  class Meta:
    db_table ='preferencia_alimentar' # preciso de def?

class NutritionalInformation(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE)
  preferencia_alimentar = models.OneToOneField(User, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)#
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)#
  description= models.CharField(max_length=100, db_column='description')
  class Meta:
    db_table ='nutricional_information' # preciso de def?

class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  #id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)#
  #weight = models.DecimalField(max_digits=8, decimal_places=1, help_text='KG_weight') #
  #height = models.DecimalField(max_digits=8, decimal_places=1, help_text='cm_weight')
  #BMI = models.DecimalField(max_digits=8, decimal_places=1, help_text='cm_weight')#
  #circumferencia_arm = models.DecimalField(max_digits=8, decimal_places=1, help_text='KG_weight') #
  #circumferencia_abdomen = models.DecimalField(max_digits=8, decimal_places=1, help_text='KG_weight') #
  #height = models.DecimalField(max_digits=8, decimal_places=1, help_text='cm_weight')
  description= models.CharField(max_length=100, db_column='description')
  class Meta:
    db_table ='antopometric_evaluation' # preciso de def?


