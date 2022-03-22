from django import forms

from user_profile.models import UserAccount

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name= forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    profile= forms.ModelChoiceField(queryset=UserAccount.objects.all(),widget= forms.Select(attrs={
        "placeholder": "Profile"
    }))
    password = forms.CharField(max_length=70, required=True)
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(max_length=70, required=True)