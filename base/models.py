from django.db import models

# Create your models here.

class users(models.Model):

  First_Name = models.CharField(max_length=50)
  Last_Name = models.CharField(max_length=50)
  Gender = models.CharField(max_length=10)
  Email = models.CharField(max_length=50)
  Passwerd = models.CharField(max_length=50)

  class Meta:
     db_table = 'form'