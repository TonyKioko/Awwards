from django import forms
from app.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile','timestamp']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user','project']
