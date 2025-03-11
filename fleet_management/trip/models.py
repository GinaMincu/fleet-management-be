from django.db import models
import datetime
from fleet_management.vehicle.models import Vehicle

class Trip(models.Model):
  vehicle = models.ForeignKey(
        Vehicle, related_name='trips', on_delete=models.CASCADE,null=True)
  driver=models.CharField(max_length=40,default="")
  start_ts=models.DateField(blank=True, null=True,default=datetime.date.today)
  end_ts=models.DateField(blank=True, null=True,default=datetime.date.today)

  def __str__(self):
        return self.driver+ "-" + self.vehicle.plate