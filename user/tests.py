from django.test import TestCase
from .models import Profile, Image, User, Comments


class ProfileTest(TestCase):

    def setUp(self):
        self.new_user = User(username='ole', email='gideonkipkirui95@gmail.com', password='3453')
        self.new_user.save()
        self.new_profile = Profile(profile_image='image.png', bio='ggg', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
   # Create your tests here.
class ImageTest(TestCase):

    def setUp(self):
        self.new_user = User(username='ole', email='gideonkipkirui95@gmail.com', password='3543')
        self.new_user.save()
        self.new_profile = Profile(profile_image='image.jpg', bio='doer', user=self.new_user)
        self.new_profile.save()
        self.new_image = Image(image_name='ggg', image='ggg.jpg', image_caption='day one', profile=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image)>0)

    

class CommentsTest(TestCase):

    def setUp(self):
        self.new_user = User(username='ole', email='gideonkipkirui95@gmail.com', password='34521')
        self.new_user.save()
        self.new_image = Image(image_name='ggg', image='ggg.jpg', image_caption='well', profile=self.new_user)
        self.new_image.save()
        self.new_comment = Comments(comment='wonderful',image=self.new_image,user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comment)>0)

   
