from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=64)
