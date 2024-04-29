from django.urls import path
from . import views
from django.urls import path
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup, name='signup'),
    
]
