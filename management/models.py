from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # igual modelo padrao com um campo bio a mais
  bio= models.TextField(blank=True)

class State(models.Model): #Tabela Estado
	
	cod_state = models.IntegerField(primary_key=True,db_column='cod_state')
	name_state = models.CharField(max_length=50,db_column='name_state')
	acrm_state = models.CharField(max_length=3,db_column='acrm_state')
	
class Meta:
	db_table ='State'

def __unicode__(self):
	return self.name_state

def __str__(self):
	return self.name_state

  
class Meal(models.Model): #Tabela Estado
	
	cod_meal = models.IntegerField(primary_key=True,db_column='cod_state')
	type_meal = models.CharField(max_length=50,db_column='type_meal')
	time_meal = models.DateTimeField(auto_now_add=True,db_column='time_meal')
	
class Meta:
	db_table ='Meal'

def __str__(self):
	return self.name_meal

def __date__(self):
	return self.time_meal

    