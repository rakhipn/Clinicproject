from django.db import models

# Create your models here.


class Admin(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class departmentdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)

class doctorsdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Category= models.CharField(max_length=100, null=True, blank=True)
    Qualification=models.CharField(max_length=100,null=True,blank=True)



