from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def main_page(request):
    return render(request,"views/main.html",{"name":"FindMoto"})