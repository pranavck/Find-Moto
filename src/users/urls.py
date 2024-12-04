from django.urls import path
from .views import login_view,RegisterView


urlpatterns = [
    path('login/',view=login_view,name='login'),
    path('register/',view=RegisterView.as_view(),name='register')
]
