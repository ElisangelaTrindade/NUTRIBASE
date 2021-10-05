from django.db import models
from cpffield import cpffield

class Patient(models.Model):
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
      return self.user.first_name + ' ' + self.user.last_name