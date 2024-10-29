from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

