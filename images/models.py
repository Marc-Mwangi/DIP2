from django.db import models

# Create your models here.
class Image(models.Model):
    
    image = models.ImageField(upload_to="photos/images")
    image_names = models.CharField(max_length=200)
    image_caption = models.CharField(max_length=2000)
    #profile = models.ForeignKey()
    likes = models.IntegerField(max_length=50000)
    comments = models.CharField(max_length=2000)
    created_at= models.DateTimeField(auto_now=True)