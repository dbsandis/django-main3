import uuid
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # date_of_birth = models.DateField(default=timezone.now)
    # Define your UserProfile fields here
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Resident(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # admission_date = models.DateField(default=timezone.now)
    # discharge_date = models.DateField(null=True, blank=True, default=timezone.now)
    # Add other resident-specific fields (e.g., address, contact info)
    def __str__(self):
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"

class Staff(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    reference_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # add other fields here
    def __str__(self):
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"