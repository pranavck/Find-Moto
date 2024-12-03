from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.contrib.auth.decorators import login_required

# Create your views here.
def main_page(request):
    return render(request,"views/main.html",{"name":"FindMoto"})


@login_required
def home_page(request):
    return render(request,"views/home.html")