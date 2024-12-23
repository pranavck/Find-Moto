from django.urls import path
from .views import login_view,RegisterView,logout_view


urlpatterns = [
    path('login/',view=login_view,name='login'),
    path('register/',view=RegisterView.as_view(),name='register'),
    path('logout/',view=logout_view,name='logout_view')
]
