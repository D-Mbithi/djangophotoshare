from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account was created successfully!')

            return redirect('/accounts/login')
    
    form = CustomUserCreationForm()

    template = 'registration/signup.html'
    context = {
        'form': form
    }

    return render(request, template, context)


def profile(request):
    template = 'profile.html'
    context = {}

    return render(request, template, context)