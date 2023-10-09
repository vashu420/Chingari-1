from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    account_type_choices = [
        ('A', 'Administrator'),
        ('P', 'Player')
    ]
    user_id = forms.CharField(max_length=255, required=False)
    identity = forms.CharField(max_length=255, required=False)
    mobile_number = forms.CharField(max_length=20, required=False)
    whatsapp_number = forms.CharField(max_length=20, required=False)
    account_type = forms.ChoiceField(choices=account_type_choices, initial='A')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_id', 'identity', 'mobile_number', 'whatsapp_number', 'account_type')
