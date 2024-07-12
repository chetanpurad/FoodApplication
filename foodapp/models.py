from django.db import models
from django.db import connection
# Create your models here.
class Details(models.Model):
    def __str__(self):
        return self.username
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)

class Items(models.Model):
    item_name=models.CharField(max_length=30)
    item_desc=models.CharField(max_length=40)
    item_price=models.IntegerField(default=0)
    item_image=models.CharField(max_length=5000,default="https://global.discourse-cdn.com/business4/uploads/inductiveautomation/original/2X/9/97d457372f6c14182b686ecfdf5d4067df5e9373.png")

    def __str__(self):
        return self.item_name

