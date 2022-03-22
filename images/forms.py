from django import forms
#from user_profile.models import UserAccount
from .models import Image
from django.forms import ModelForm

class UploadForm(ModelForm):
    class Meta:
        model = Image
        fields =('image','image_caption',)
    
    #image = forms.FileField()
    #image_caption= forms.CharField(max_length=2000)
    #image_name = forms.CharField(max_length=200)
    #profile = forms.ModelChoiceField(queryset= UserAccount.objects.all(),widget= forms.Select(attrs={
    #    "placeholder" :'Profile'
    #}))
class SignUpForm(forms.Form):
    firstname=forms.CharField( max_length=30, required=True)
    lastname=forms.CharField( max_length=30, required=True)
    username =forms.CharField( max_length=30, required=True)
    email = forms.EmailField(label="Email")