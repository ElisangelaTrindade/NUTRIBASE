from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser): # igual modelo padrao com um campo bio a mais
  bio= models.TextField(blank=True)