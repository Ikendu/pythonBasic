from django.db import models

# Create your models here.
class Students(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  email = models.EmailField(null=True)
  school = models.CharField(max_length=255, null=True)
