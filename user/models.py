from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django .utils import timezone
# Create your models here.
class Image (models.Model):
    image = CloudinaryField('images',blank = True)
    image_name = models.CharField(max_length=55)
    image_caption = models.CharField(max_length=55)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete = models.CASCADE)
    likes = models.PositiveIntegerField(defaiult = 0)
    date_posted = models.DateTimeField(default=timezone)
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

    def likes(self):
        return self.likes.count()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(blank = True,max_length = 30)
    email = models.CharField(blank = True, max_length = 100)
    bio = models.TextField(max_length=100)
    profile_image = models.ImageField(upload_to = 'images/')
    follow = models.ManyToManyField(User, related_name='follows',blank = True)
    
    # def __str__(self):
    #     return self.profile_image.url

    # def save_profile(self):
    #     self.save()
        
    # @classmethod
    # def get_profile(cls,id):
    #     profile = Profile.objects.all()
    #     return profile
        
    # @classmethod
    # def update_profile(cls,id,new_name):
    #     cls.objects.filter(id=id).update(name = new_name)

    # @classmethod
    # def delete_profile(cls,id):
    #     cls.objects.filter(id).delete()


    # @classmethod
    # def search_by_name(cls, searched_name):
    #     username = cls.objects.filter(name__icontains=searched_name)

    #     return username



class Comments(models.Model):
    comment = models.TextField(blank = True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank = True)
    image = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)     

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()
    
    
    @classmethod
    def update_comment(cls,id,new_comment):
        cls.objects.filter(id=id).update(comment = new_comment)
        
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments
    

    @classmethod
    def delete_comment(cls,id):
        cls.objects.filter(id).delete()
 

    
