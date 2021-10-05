from django.db import models

# Create your models here.
class Meal(models.Model):
  registered_by = models.OneToOneField(User, on_delete=models.CASCADE)
  food_diary = models.ForeignKey(FoodDiary, on_delete=models.CASCADE)
  diet_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
  type_meal = models.CharField(max_length=50,db_column='type_meal')
  time_meal = models.DateTimeField(db_column='time_meal')

  class Meta:
    db_table ='meal'