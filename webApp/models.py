from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImageModel(models.Model):
    name = models.CharField(null=False, max_length=100)
    cover = models.ImageField(upload_to='images/')
    tone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username