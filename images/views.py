from django.shortcuts import render
from .forms import UploadForm
# Create your views here.
def Images(request):
    
    form = UploadForm()
    
    #Outputs
    context = {
        "form": form
    }
    
    return render(request, 'index.html', context)

def Feed(request):
    
    form = UploadForm()
    
    #Outputs
    context = {
        "form": form
    }
    
    return render(request, 'feed.html', context)