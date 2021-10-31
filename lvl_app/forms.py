from django import forms
from django.contrib.auth.models import User
from lvl_app.models import UserInfoProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForms(forms.ModelForm):
    class Meta():
        model = UserInfoProfile
        fields = ('user_portfolio_site', 'user_dp')
