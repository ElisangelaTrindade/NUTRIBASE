from django.db import models

# I created the app User
"""from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser): # igual modelo padrao com um campo bio a mais
  bio= models.TextField(blank=True)"""

# state and city sent to location
"""class State(models.Model):
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
  name_city = models.CharField(max_length=100, db_column='name_city')

  class Meta:
    db_table ='city'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.name_state"""

# the classes below FamilyHealthHistory and PatientHealthHistory were sent to the HealthHistory's app
"""class FamilyHealthHistory(models.Model):
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField (db_column='hypertension')
  cancer = models.BooleanField (db_column='cancer')
  diabetes = models.BooleanField (db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField( db_column='others')
  class Meta:
    db_table ='family_health_history' 

class PatientHealthHistory(models.Model):
  obesity = models.BooleanField(db_column='obesity')
  cardiovascular_disease = models.BooleanField( db_column='cardiovascular_disease')
  hypertension = models.BooleanField(db_column='hypertension')
  cancer = models.BooleanField(db_column='cancer')
  diabetes = models.BooleanField( db_column='diabetes')
  dyslipidemia = models.BooleanField(db_column='dyslipidemia')
  others = models.TextField (db_column='others')

  class Meta:
    db_table ='patient_health_history' """

# the class below was sent to the Patient's app
 """class Patient(models.Model): 
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  family_health_history = models.ForeignKey(FamilyHealthHistory, on_delete=models.CASCADE)
  patient_health_history = models.ForeignKey(PatientHealthHistory, on_delete=models.CASCADE)
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50, db_column='street')
  city = models.OneToOneField(City, on_delete=models.CASCADE)
  zip_code = models.CharField(max_length=15,default = '', db_column='zip_code')

  GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
    )
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

  class Meta:
    db_table ='patient'
    def __str__(self):
      return self.user.first_name + ' ' + self.user.last_name """


# the classes Exercise and ExerciseType were sent to the app Exercise
"""class ExerciseType(models.Model):
  name = models.CharField(max_length=255, db_column='type')

class Exercise(models.Model):
  exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  frequency = models.CharField(max_length=255, db_column='frequency')
  def __str__(self):
    return self.type+ self.patient.frequency"""

# the class Employee was sent to the app employee
"""class Employee(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  hire_date = models.DateField(db_column='hire_date')
  #type = models.CharField(max_length=50,db_column='type')#
  cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
  birthday = models.DateField()
  email = models.CharField(max_length=150,db_column='email_patient')
  street = models.CharField(max_length=50, db_column='street')
  city = models.OneToOneField(City, on_delete=models.CASCADE)
  zip_code = models.CharField(max_length=9,default = '')
    
  class Meta:
    db_table ='employee'
    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name"""

# the class Phone was sent to the app phone
"""class Phone(models.Model):
  patient =models.ForeignKey(Patient, on_delete=models.CASCADE) #ta errado?
  phone_number = models.CharField(max_length=14, db_column='phone_number')
  description = models.TextField(db_column='description')
  
  class Meta: 
    db_table ='phone' 
    def __str__(self):
      return self.phone_number"""

# the class foodDiary was sent to the app fooddiary
"""class FoodDiary(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_consultation=models.DateField()
  weight=models.DecimalField(max_digits=4, decimal_places=1, db_column='weight')

  class Meta:
    db_table ='food_diary'"""


# the class DietPlan  was sent to the app DietPlan
"""class DietPlan(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_creation=models.DateField()
  amount_of_calories=models.DecimalField(max_digits=8, decimal_places=1, db_column='amount_of_calories')
  weigh=models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  class Meta:
    db_table ='diet_plan' """

# the class Meal  was sent to the app Meal
"""class Meal(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  food_diary = models.ForeignKey(FoodDiary, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  type_meal = models.CharField(max_length=50,db_column='type_meal')
  time_meal = models.DateTimeField(db_column='time_meal')

  class Meta:
    db_table ='meal'"""

# the class FoodGroup and Food  were sent to the app food_group
"""class FoodGroup(models.Model): 
  group = models.CharField(max_length=150,db_column='group')
  weight = models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  calories = models.PositiveIntegerField(default=0, db_column='calories')

  class Meta:
    db_table ='food_group' 

class Food(models.Model):
  food_group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
  diet_plan = models.OneToOneField(DietPlan, on_delete=models.CASCADE)
  food_name=models.CharField(max_length=50, db_column='food_name')
  weigh=models.DecimalField(max_digits=8, decimal_places=1, db_column='weight')
  
  class Meta:
    db_table ='food' """


# the classes below foodComsumption, foodIntolerance and foodPreferences were sent to the foodConsuption's app
"""class FoodConsumption(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  soft_drink = models.BooleanField (db_column='soft_drink')
  candy = models.BooleanField(db_column='candy')
  deep_fried = models.BooleanField( db_column='deep_fried')
  fast_food= models.BooleanField( db_column='fast_food')
  processed_food = models.BooleanField( db_column='processed_food')
  canned_food = models.BooleanField( db_column='canned')
  fruits = models.BooleanField( db_column='fruits')
  vegetables = models.BooleanField( db_column='vegetables')
  others = models.TextField(db_column='description')
  class Meta:
    db_table ='food_consumption' 

class FoodIntolerance(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  intolerance_description= models.TextField(db_column='intolerance_description')
  class Meta:
    db_table ='food_intolerance' 

class FoodPreferences(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  class Meta:
    db_table ='food_preferences' """

# the classe below NutritionalConduct were sent to the nutricional_information's app
"""
class NutritionalConduct(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  food_intolerance = models.OneToOneField(FoodIntolerance, on_delete=models.CASCADE)
  food_preferences = models.OneToOneField(User, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  food_consumption = models.ForeignKey(FoodConsumption, on_delete=models.CASCADE)
  caloric_needs = models.DecimalField(max_digits=4, decimal_places=2, db_column='caloric') 
  additional_information= models.TextField(db_column='additional_information')

  class Meta:
    db_table ='nutricional_information' """

   
# the classe below AntopometricEvaluation were sent to the antopometric_evaluation's app
"""class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registeres_by = models.OneToOneField(User, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=6, decimal_places=2, db_column='weight') 
  height = models.CharField(max_length=4,db_column='height')
  BMI = models.DecimalField(max_digits=4, decimal_places=2, db_column='ibm')
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='arm_circumference') 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='abdomen_circumference') 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='wrist_circumference')
  date_of_consultation=models.DateField()
  updated=models.DateField()
  additional_information= models.TextField(db_column='additional_information')
  class Meta:
    db_table ='antopometric_evaluation' """

# the class below LabExams were sent to the ClinicEvaluation's app 
"""class LabExam (models.Model): 
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  register_by = models.OneToOneField(User, on_delete=models.CASCADE)
  name_exam =models.CharField(max_length=100, db_column='description')
  date_of_exam=models.DateField()
  upload=models.FileField( db_column='upload')
  exam_information= models.TextField(db_column='name_exam ')
  class Meta:
    db_table ='lab_exam'        """

# the classes below ClinicEvaluation, GastrointestinalTractSymptoms were sent to the ClinicEvaluation's app 

"""class ClinicEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  nails= models.CharField(max_length=100, db_column='nails')
  skin = models.CharField(max_length=100, db_column='skin')
  bladder_habits = models.CharField(max_length=100, db_column='bladder_habits')
  bowel_habits = models.CharField(max_length=100, db_column='bowel_habits') 
  additional_information= models.TextField(db_column='additional_information')
  date_of_consultation=models.DateField()
  updated=models.DateField()
  class Meta:
    db_table ='clinic_evaluation' 

class GastrointestinalTractSymptoms(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  dysphagia = models.BooleanField (db_column='dysphagia')
  pain= models.BooleanField(db_column='pain')
  reflux = models.BooleanField( db_column='reflux')
  heart_burn= models.BooleanField( db_column='heart_burn')
  constipation = models.BooleanField( db_column='constipation')
  nausea= models.BooleanField( db_column='nausea')
  diarrhea= models.BooleanField( db_column='diarrhea')
  others = models.TextField(db_column='description')
  class Meta:
    db_table ='gastrointestinalt_tract_symptoms' """

