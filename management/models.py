from django.db import models
from cpffield import cpffield
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # igual modelo padrao com um campo bio a mais
  bio= models.TextField(blank=True)

class State(models.Model): #Tabela Estado
  name_state = models.CharField(max_length=50,db_column='name_state')
  acrm_state = models.CharField(max_length=3,db_column='acrm_state')

  class Meta:
    db_table ='state'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.name_state

class City(models.Model): #Tabela Estado
  name_city = models.CharField(max_length=50,db_column='name_city')
  state = models.OneToOneField(State, primary_key=True, on_delete=models.CASCADE)

  class Meta:
    db_table ='city'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.name_state
  
class Meal(models.Model): 
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
    db_table ='food_group' # parei de por o def aqui

class Patient(models.Model):
    register_by = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
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

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Employee(models.Model):
    register_by = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=50,db_column='type')
    cpf = cpffield.CPFField('CPF', max_length=14, unique=True)
    birthday = models.DateField()
    email = models.CharField(max_length=150,db_column='email_patient')
    street = models.CharField(max_length=50)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=9,default = '')

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name


# irei por telefones de contato?
# tenho que atualizar as tabelas



