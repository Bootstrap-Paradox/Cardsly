from django import forms

from .models import username_validation

import re


# Create the Forms below


class LoginForm(forms.Form):
    login_text = forms.CharField(max_length=250,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username", "name":"username", "autocomplete": "off", "type": "text"}),
        help_text="Username or Email can be Used to Login",
        error_messages={"required": "Please enter Username or Email"},
        required=True
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "name": "password"})
        )







class SignupForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"placeholder":"Username", "name": "username", "autocomplete":"off", "type":"text"}) ,label="")
    email = forms.EmailField(max_length=250,label="", widget=forms.TextInput(attrs={"placeholder": "Email", "name": "email"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "Password", "name":"password"}), label="")
    confirm_password = forms.CharField( widget= forms.PasswordInput(attrs={"placeholder": "Confirm Password", "name":"confirm_password"}), label="")


    def clean_username(self):
        print(self.data['username'])
        if not username_validation(self.data['username']):
            raise forms.ValidationError("Username Taken")

        # if re.search("[\n\t\b\\\'\"!@#$%^&*()=+-~`/?,<>\[\]\{\}]", self.data['username']):
        #     raise forms.ValidationError("Special Characters not Supported")

        if re.search("[^a-zA-Z0-9._]", self.data['username']):
            raise forms.ValidationError("Special Charaters")

        return self.data["username"]

    def clean_password(self):
        value = self.data['password']

        if len(value) < 8:
            raise forms.ValidationError("Password must be at least 8 Characters")

        if len(value) > 150:
            raise forms.ValidationError("Password must be Less than 150 Characters")

        if not re.search("[1-9]", value):
            raise forms.ValidationError("Passwords must Contain Numbers")

        
        return self.data["password"]


    def clean_confirm_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Passwords must match')

        return self.data["confirm_password"]

    def check_password_security(self):
        if self.password == self.username:
            return (False, "Password Too Similar to Username")
