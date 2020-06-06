from django.db import models
from django.contrib.auth.models import User
from home.models import UserProfile

class store_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    store_name =  models.CharField(max_length=100)
    #piture of the store 
    link_store_website = models.CharField(max_length=300)
    adress = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=40)
    blurb_about_store = models.CharField(max_length=400)
    verified = models.BooleanField(default=False)
    

class store_event_post(models.Model):
    store = models.ForeignKey(store_user, on_delete=models.CASCADE, unique=False, default = 1)
    event_title = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.CharField(max_length=100)
    event_format = models.CharField(max_length=100)
    event_discription = models.CharField(max_length=400)
    views = models.IntegerField(default=0)

class store_promotion_post(models.Model):
    store = models.ForeignKey(store_user, on_delete=models.CASCADE, unique=False, default = 1)
    promotion_title = models.CharField(max_length=100)
    promotion_discription = models.CharField(max_length=400)
    views = models.IntegerField(default=0)

    #picture

class follow_store(models.Model):
    store = models.ForeignKey(store_user, on_delete=models.CASCADE, unique=False)
    follower =  models.ForeignKey(UserProfile, on_delete=models.CASCADE)