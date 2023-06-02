from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "You may had entered an invalid username or password, Try Again...")
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


def login_modal(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('home')
            elif user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "You may have entered an invalid username or password. Try again...")
                messages.success(request, "Your account may be deactivated by the admin...")
                return redirect('home')
        except Exception as e:
            messages.error(request, "An error occurred while trying to log in. Please try again later.")
            return render(request, 'user/error_page.html', {'error': str(e)})
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    messages.success(request, "You Are Now Logged Out...")
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Are Now Registered...")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form': form,})
