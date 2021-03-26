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
    
    def save_image(self):
        self.save()
    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images
    @classmethod
    def get_single_photo(cls,id):
        image = cls.objects.get(pk=id)
        return image
    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def display_images(cls):
        image = cls.objects.all()
        return image
    @classmethod
    def update_caption(cls,id,new_caption):
        cls.objects.filter(id=id).update(image_caption=new_caption)

    

    

    
