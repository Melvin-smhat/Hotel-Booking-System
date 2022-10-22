from tkinter import Widget
from django import forms
from django import forms
from general.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    widget={
                'password':forms.PasswordInput(),
            }
    class Meta:
        model= CustomUser
        fields=('email','first_name','last_name','occupation','password','passport')
        
    def clean_password(self):
        password=self.cleaned_data.get('password', None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password
            
        return make_password(password)
        
        