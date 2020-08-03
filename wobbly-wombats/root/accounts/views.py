from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
