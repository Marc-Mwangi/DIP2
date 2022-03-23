from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class AccountManager(BaseUserManager):
    
    #Create user method
    def create_user(self, first_name, last_name, email ,user_name, password=None):
        #Check if email exists
        if not email:
            raise ValueError("User must have an email address")
        if not user_name:
            raise ValueError("User must have a usernname")
        
        #save user
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        
        #user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, first_name, last_name, email ,user_name, password):
            
        user = self.model(
        email = self.normalize_email(email),
        user_name = user_name,
        first_name = first_name,
        last_name = last_name,
        password = password
    )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        
        user.set_password(password)    
        user.save(using= self._db)
        
        return user
            
        
    
class UserAccount(AbstractBaseUser):
    
    user_name= models.CharField(max_length=1000)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    profile_photo = models.ImageField( upload_to='photos/user_profile', blank=True)
    profile_slug= models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=4000, blank=True)
    
    #Required fields
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    #Change admin login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    
    objects = AccountManager()
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True