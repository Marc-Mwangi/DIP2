from email.policy import default
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
    
    #Required fields
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default= False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user_name