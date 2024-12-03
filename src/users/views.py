from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

def login_view(request):
    if request.method =='POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(password=password,username=username)
            print("user",user)
            if user is not None:
                login(request,user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request,f"An error occured during authentication")
        else:
            messages.error(request,f"An error occured during authentication")
        #return render(request, "views/login.html",{"login_form":login_form})
    elif request.method=='GET':   
        login_form = AuthenticationForm()
    return render(request, "views/login.html",{"login_form":login_form})
