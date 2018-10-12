from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to='profpics/',default='NO IMAGE')
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User, null=True)
    contact = models.CharField(max_length=60,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    @classmethod
    def search_by_username(cls,search_term):
        users = cls.objects.filter(user__username__icontains=search_term)
        return users

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile
    @classmethod
    def profile_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
