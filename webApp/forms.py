from django import forms
from django.db.models import fields
from .models import ImageModel
from .models import UserProfileInfo
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = ['name',  'cover']
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
