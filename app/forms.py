from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import UserModel


class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='Conform Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

    class Meta:
        model = UserModel
        fields = ("email","password1","password2")
        error_messages = {
        'email': {
            'unique': ("Email Address already Registered. Please Login."),
           },
        }
        

        widgets={
            'email':forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Email Address'}),
            
            
        }

class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model=UserModel
        fields=('email','password')

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),
         }

    
         
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Credentials")
