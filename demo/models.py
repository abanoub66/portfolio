from django.db import models


# Create your models here.
class Demo(models.Model):
    number_list = models.CharField(max_length=200)
