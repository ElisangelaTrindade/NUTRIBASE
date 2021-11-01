from django.db import models
from patient.models import Patient
from user.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class AntopometricEvaluation (models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  weight = models.DecimalField(max_digits=6, decimal_places=2, db_column='weight') 
  height = models.CharField(max_length=4,db_column='height')
  BMI = models.DecimalField(max_digits=4, decimal_places=2, db_column='ibm')
  arm_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='arm_circumference') 
  abdomen_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='abdomen_circumference') 
  wrist_circumference = models.DecimalField(max_digits=4, decimal_places=2, db_column='wrist_circumference')
  date_of_consultation=models.DateField()
  updated=models.DateField()
  additional_information= models.TextField(db_column='additional_information')
 

  def __str__(self):
      return self.patient.first_name + " " + self.patient.last_name
  
  class Meta:
    db_table ='antopometric_evaluation' 

@receiver(pre_save, sender=User.username)
def registered_by_pre_save(sender, instance, *args, **kwargs):
   if instance.registered_by is True:
    instance.registered_by=(instance.User.username)

pre_save.connect(receiver=registered_by_pre_save, sender=registered_by_pre_save)