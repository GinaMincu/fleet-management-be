from django.db import models

# Create your models here.
class Vehicle(models.Model):
  plate=models.CharField(max_length=40,default="")
  model=models.CharField(max_length=100,default="")
  color=models.CharField(max_length=40,default="")

  def __str__(self):
        return self.plate