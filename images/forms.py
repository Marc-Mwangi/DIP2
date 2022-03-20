from cProfile import label
from django import forms


class UploadForm(forms.Form):
    
    image = forms.FileField()
    image_caption= forms.CharField(max_length=2000)
    
class SignUpForm(forms.Form):
    firstname=forms.CharField( max_length=30, required=True)
    lastname=forms.CharField( max_length=30, required=True)
    username =forms.CharField( max_length=30, required=True)
    email = forms.EmailField(label="Email")