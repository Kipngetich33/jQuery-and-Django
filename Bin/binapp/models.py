
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name


class Lion(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

