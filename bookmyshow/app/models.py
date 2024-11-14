from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.TextField
    date=models.DateField
    bck_img=models.FileField
    for_img=models.FileField
    lang=models.TextField
    dim=models.TextField
    dur=models.TextField
    type=models.TextField
    cert=models.TextField
    about=models.TextField
