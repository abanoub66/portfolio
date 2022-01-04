from django.db import models


# Create your models here.
class Demo(models.Model):
    number_list = models.CharField(max_length=200)


class SortingMethod(models.Model):
    sorting_method = models.CharField(max_length=50)
