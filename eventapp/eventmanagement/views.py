from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EventRegistrationForm 
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request, 'eventmanagment/home.html')

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)  # ✅ built-in check
        if user is not None:
            login(request, user)   # ✅ start session
            return redirect('home')
        else:
            return render(request, 'eventmanagment/login.html', {'error': 'Invalid credentials'})
    return render(request, 'eventmanagment/login.html')




def register_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            # save event details
            event = form.save(commit=False)
            event.save()

            # also create user (with password)
            username = form.cleaned_data.get('email')  # using email as username
            password = form.cleaned_data.get('password')

            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password, email=username)
            
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = EventRegistrationForm()
    return render(request, 'eventmanagment/register.html', {'form': form})
