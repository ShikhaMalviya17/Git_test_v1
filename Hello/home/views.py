from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

def index(request):
    context = {
        'variable' : 'This is sent'
    }

    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')


def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())

        contact.save()
        messages.success(request,'Thank you for contacting us, your message has been sent !!')

    return render(request,'contact.html')
