from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail ,BadHeaderError
from django.conf import settings

from user_profile.models import UserAccount
from user_profile.forms import RegistrationForm,LoginForm

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
            return HttpResponseRedirect('/accounts/login')
    form = RegistrationForm()
    context={
        "form" : form
    }
    return render(request, 'signup.html', context=context)