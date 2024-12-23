from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.contrib.auth.decorators import login_required
from main.models import Listing

# Create your views here.
def main_page(request):
    return render(request,"views/main.html",{"name":"FindMoto"})


@login_required
def home_page(request):
    listing = Listing.objects.all()
    context = {
        "listings":listing
    }
    return render(request,"views/home.html",context)


def list_view(request):
    if request.method == 'POST':
        pass
    elif request.method== 'GET':
        pass
    return render(request,"views/list.html",{})