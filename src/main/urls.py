from django.urls import path
from main.views import main_page,home_page,list_view


urlpatterns = [
    path('',main_page,name='main'),
    path('home/',home_page,name="home"),
    path('list/',list_view,name="list")
]
