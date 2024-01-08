from django.db import models
from django.contrib.auth.models import User

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add other fields here

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add other fields here

# add other models here