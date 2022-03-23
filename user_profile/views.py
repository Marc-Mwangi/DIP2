from django.shortcuts import render,HttpResponseRedirect, redirect
from django.core.mail import send_mail ,BadHeaderError
from django.conf import settings
from django.contrib.auth import authenticate, login as user_login , logout as user_logout
from user_profile.models import UserAccount
from user_profile.forms import RegistrationForm,LoginForm
from images.views import Feed
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        user_name = email.split('@')[0]
        password = request.POST.get("password")
        
        user = UserAccount.objects.create_user(first_name=first_name, last_name=last_name,email=email, password=password,user_name=user_name)
        user.save()
        
        if user:
            return HttpResponseRedirect('login')
    form = RegistrationForm()
    context={
        "form" : form
    }
    return render(request, 'signup.html', context=context)

def login(request):
    
    if request.method == "POST":
        email= request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None :
            
            user_login(request, user)
            
            return  HttpResponseRedirect('feed')
        else:
            return redirect('feed')
    form = LoginForm
    context={
        "form" : form
    }
    
    return render(request, 'login.html', context=context)