from django.db import models

# Create your models here.
class Vehicle(models.Model):
  plate=models.CharField(max_length=40)
  model=models.CharField(max_length=100)
  color=models.CharField(max_length=40)