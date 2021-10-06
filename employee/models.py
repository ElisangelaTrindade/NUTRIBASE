from django.db import models
from cpffield import cpffield

class Employee(models.Model):
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
        return self.user.first_name + ' ' + self.user.last_name