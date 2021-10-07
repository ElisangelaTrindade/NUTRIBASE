from django.db import models


class State(models.Model):
  name = models.CharField(max_length=50,db_column='state')
  acrm= models.CharField(max_length=3,db_column='acrm')

  class Meta:
    db_table ='state'

    def __unicode__(self):
      return self.name

    def __str__(self):
      return self.acrm

class City(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  city = models.CharField(max_length=100, db_column='city')

  class Meta:
    db_table ='city'

    def __unicode__(self):
      return self.state

    def __str__(self):
      return self.city
