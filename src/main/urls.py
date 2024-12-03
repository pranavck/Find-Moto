from django.urls import path
from main.views import main_page,home_page


urlpatterns = [
    path('',main_page,name='main'),
    path('home',home_page,name="home")
]
