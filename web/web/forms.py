'''
Created on 22/1/2015

@author: E457035
'''

from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__" 