from django.shortcuts import render,redirect
from .models import LoginData
from .models import SignupData
def homepage(request):
    return render(request,'homepage.html')
def gallerypage(request):
    return render(request,'gallerypage.html')
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        LoginData(
        email=request.POST.get('user_name')
        password=request.POST.get('password')
        )

def signup(request):
    if request.method='GET':
        return render(request,'signup.html')
    else:
        SignupData(
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        dob=request.POST.get('dob')
        Email=request.POST.get('Email')
        phone=request.POST.get('phone')
        ).save()
        return redirect('homepage')
# Create your views here.
