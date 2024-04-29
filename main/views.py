from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from .models import *
from .forms import UserForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            render(request, 'home.html')  # Change 'signup_success' to the URL of your success page
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})