from django.db import models
from user_profile.models import UserAccount

# Create your models here.
class Image(models.Model):
    
    image = models.ImageField(upload_to="images/")
    #image_slug = models.CharField(max_length=200)
    image_caption = models.CharField(max_length=2000)
    #profile = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    #likes = models.IntegerField()
    #comments = models.CharField(max_length=2000)
    #created_at= models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.image_caption