from django.db import models

# Create your models here.
class FoodDiary(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  description= models.TextField(db_column='description')
  date_of_consultation=models.DateField()
  weight=models.DecimalField(max_digits=4, decimal_places=1, db_column='weight')

  class Meta:
    db_table ='food_diary'
