from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user_instance=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile_image/',default="profile.jpg")
    full_name=models.CharField(max_length=30,blank=True)
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=50,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    email=models.EmailField(blank=True)
    phone=models.CharField(max_length=12,blank=True)
    website=models.URLField(blank=True)
