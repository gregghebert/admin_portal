from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput
from django.utils.translation import gettext_lazy as _
from .models import UserInfo
from django.core.exceptions import ValidationError
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ['fullName', 'email', 'password', 'confirm_password']
        labels = {
            'fullName': _('Your Full Name'),
            'email': _('Your Email'),
            'password': _('Your Password'),
            'confirm_password': _('Confirm Password'),
        }

    def clean_name(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        fullName = self.cleaned_data['fullName'].lower()
        r = User.objects.filter(fullName=fullName)
        if not fullName.isalpha():
            raise forms.ValidationError("Invalid Name")
        return fullName

    def clean_email(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        if not (re.search(regex, email)):
            raise ValidationError("Invalid Email")
        return email

    def clean_password(self):
        SpecialSym = ['$', '@', '#', '%']
        cleaned_data = super(UserRegisterForm, self).clean()

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    "The two password fields must match.")
        if len(password) < 6:
            raise forms.ValidationError("Password length should be at least 6")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError(
                'Password should have at least one numeral')
        if not any(char.isupper() for char in password):
            raise forms.ValidationError(
                'Password should have at least one uppercase letter')
        if not any(char in SpecialSym for char in password):
            raise forms.ValidationError(
                'Password should have at least one of the symbols $@#')
        return confirm_password
