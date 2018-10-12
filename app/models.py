from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to='profpics/',default='NO IMAGE')
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User, null=True)
    contact = models.CharField(max_length=60,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = models.ImageField(upload_to='projectpics/',default='NO IMAGE')
    description = models.CharField(max_length=60,blank=True)
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
