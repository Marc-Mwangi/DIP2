from email.mime import image
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import UploadForm
from .models import Image
from django.core.files.storage import FileSystemStorage

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
    form = UploadForm
    context= {
       "form":form, 
    }
    if request.method == "POST" :
    
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            context={
                    "form": form,
                    "img_obj": img_obj,
                }
            return render(request, 'feed.html', context)
       
    
    return render(request, 'feed.html', context)