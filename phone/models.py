from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

class Phone(models.Model):
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name = _('content_type'))
  object_id = models.PositiveIntegerField(verbose_name = _('object_id'))
  content_object = GenericForeignKey('content_type', 'object_id')
  phone_number = models.CharField(max_length=14, db_column='phone_number', verbose_name= _('phone number'))
  description = models.CharField(max_length=200,db_column='description', verbose_name= _('description'))
  
  class Meta: 
    db_table ='phone' 
    verbose_name = _('Phone')
    verbose_name_plural = _('Phones')

  def __str__(self):
    return self.phone_number
