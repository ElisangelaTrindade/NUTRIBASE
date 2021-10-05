from django.db import models


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
  name_city = models.CharField(max_length=100, db_column='name_city')

  class Meta:
    db_table ='city'

    def __unicode__(self):
      return self.name_state

    def __str__(self):
      return self.name_state
