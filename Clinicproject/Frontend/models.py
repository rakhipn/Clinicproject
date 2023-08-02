from django.db import models

# Create your models here.

class appointmentdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Department = models.CharField(max_length=100,null=True, blank=True)
    Doctor = models.CharField(max_length=100,null=True, blank=True)
    Datetime = models.DateTimeField()
    Place = models.CharField(max_length=100, null=True, blank=True)


class regdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_password=models.CharField(max_length=100,null=True,blank=True)