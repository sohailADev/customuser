from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from django.contrib.auth.decorators import login_required
from customuser_app import forms
from django.contrib.auth import authenticate, login,logout
from customuser_app import models
from django.conf import settings

@login_required
def index_view(request):
    setting_auth_user_model = settings.AUTH_USER_MODEL
    return render(request,'home.htm',{'setting_auth_user_model':setting_auth_user_model})

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data         
            user = authenticate(request, username=data.get('username'), password=data.get('password'))          
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
      
    form = forms.LoginForm()
    return render(request,'login.htm',{'form':form})

def signup_view(request):  
        if request.method == "POST":
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                u_name = data.get('username')
                u_pass = data.get('password')
                u_displayname = data.get('displayname')
                signup_user = models.CustomUserModel.objects.create_user(username = u_name,password=u_pass,displayname=u_displayname)
                if signup_user:
                    login(request,signup_user)
                    return HttpResponseRedirect(reverse("login_page"))
        form = forms.SignUpForm()
        return render(request,"signup.htm",{'form':form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_page"))