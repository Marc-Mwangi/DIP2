from django.db import models

# Create your models here.
class UserProfile(models.Model):
    
    user_name= models.CharField(max_length=1000)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='photos/user_profile')
    profile_slug= models.CharField(max_length=200)
    bio = models.CharField(max_length=4000)
    
    def __str__(self) -> str:
        return self.user_name