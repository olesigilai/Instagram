from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Image (models.Model):
    image = CloudinaryField('images',blank = True)
    image_name = models.CharField(max_length=55)
    image_caption = models.CharField(max_length=55)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete = models.CASCADE)
    likes = models.PositiveIntegerField(defaiult = 0)

    def __str__(self):
        return self.image_name
    
