from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,ReadOnlyPasswordHashField

# class pinho(forms.Form):
#     # pin= forms.ChoiceField(label='Pin', widget=forms.RadioSelect(choices=[('True','False')])
#     something_truthy = forms.BooleanField(required=False)


