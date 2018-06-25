
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.data

    @classmethod
    def get_data(cls):
        latest = cls.objects.first()
        return latest

class Lion(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name