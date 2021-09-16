from django.db import models

# Create your models here.

class Position(models.Model):# created position subclass of Model class
    title = models.CharField(max_length=100) 

    def __str__(self):
        return self.title # This is to object into readable form

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=11)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)#Here used position as a foriegn key so that we used this when we want to delete data.
    