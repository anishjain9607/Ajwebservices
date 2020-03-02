from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail

from . import urls
# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are now Logged in")
            return redirect('index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:    
        return render(request,'accounts/login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')    
def signup(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['emailid']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request,'This Username is Taken')
            return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request,'This Email_id is Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
                )
                messages.success(request,"Your account is created")
                return redirect('login')

    else:    
        return render(request,'accounts/signup.html')