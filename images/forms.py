from django import forms


class UploadForm(forms.Form):
    
    #image = forms.ImageField(upload_to= "photos/images")
    image_caption= forms.CharField(max_length=2000)
    