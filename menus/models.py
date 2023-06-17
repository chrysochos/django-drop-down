from django.db import models

# Create your models here.

# Path: menus\models.py
# create District
class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# create Person from a District
class Person(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    