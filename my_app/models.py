from django.db import models

class UserLogin(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    email = models.CharField

# Create your models here.
