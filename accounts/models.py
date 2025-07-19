from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='user_profile')

    def __str__(self):
        return self.bio