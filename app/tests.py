from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone
# Create your tests here.
class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='tony')
        self.user.save()
        self.profile = Profile(photo='black and white',bio='test bio',contact="abc@xyz.com",user=self.user)
        self.profile.save_profile()


    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.project = Project(title ='new project', image='image.url',description="awwaaards",link="http://www.awwaards.com")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)
    def test_delete_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)
