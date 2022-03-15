from django.shortcuts import render
from .forms import UploadForm
from .models import Image

# Create your views here.
def Images(request):
    
    Image.objects.all()
    picture = Image.objects.all()
    
    form = UploadForm()
    
    #Outputs
    context = {
        "form": form
    }
    
    return render(request, 'index.html', context)

def Feed(request):
    
    Image.objects.all()
    picture = Image.objects.all()
    
    
    form = UploadForm()
    
    #Outputs
    context = {
        "form": form,
        "picture": picture
    }
    
    return render(request, 'feed.html', context)