from django.db import models

# Create your models here.
from django.db.models import IntegerField


class Tasktable(models.Model):
    name=models.CharField(max_length=255)
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.name