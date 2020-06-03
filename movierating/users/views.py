from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationFrom

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Please log in.')
            return redirect('login')
    else:
        form = UserRegisterationFrom()
    return render(request, 'users/register.html', {'form': form})
