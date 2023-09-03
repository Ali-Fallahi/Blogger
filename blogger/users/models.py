from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, default="name")
    image = models.ImageField(default='profilepic.jpg',
                              upload_to='profile_pictures')

    def __str__(self):
        return self.user.username
