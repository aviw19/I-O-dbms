# models.py
from django.db import models
class User(models.Model):
    sid = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    def __str__(self):
        return self.name