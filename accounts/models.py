from django.db import models


# Create your models here.

class ProjectInfo(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    favicon = models.ImageField(upload_to='images')
