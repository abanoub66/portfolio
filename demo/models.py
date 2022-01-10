from django.db import models


class Demo(models.Model):
    number_list = models.CharField(max_length=200)
