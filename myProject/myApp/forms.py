from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'email', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')       