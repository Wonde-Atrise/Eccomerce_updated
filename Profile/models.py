from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class Profile(models.Model):
            user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
            birth_date = models.DateField(null=True, blank=True)
            phone_number = models.CharField(max_length=20, blank=True)
            profile_image = models.ImageField(null=True,blank=True,upload_to='images/')
           
            def photo_url(self):
             if self.photo:
                return self.photo.url
             return '/static/images/default_profile.png' # Or some default path
        
