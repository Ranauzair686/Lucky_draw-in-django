from django.db import models

# Create your models here.

class Myinfo(models.Model):
    name  = models.CharField(max_length=50)
    bio   = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/')