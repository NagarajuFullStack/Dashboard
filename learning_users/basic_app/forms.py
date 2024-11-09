from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        # include = ['porfolio_site','profile_pic','id_number','position','compeny']
        include = ['profile_pic','id_number','position','compeny','Email_address','phone']
        exclude = ['user']
