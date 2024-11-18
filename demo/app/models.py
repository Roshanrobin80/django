from django.db import models


# Create your models here.
class Student(models.Model):
    roll_nmuber=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
