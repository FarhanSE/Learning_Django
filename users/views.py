from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profiles
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def single_profile(request, pk):
    profile = Profiles.objects.get(id=pk)
    topskills = profile.skills_set.exclude(description__exact="")
    otherskills = profile.skills_set.filter(description="")
    context = {'profile':profile, "topskills":topskills, "otherskills":otherskills}
    return render(request, 'users/single_profile.html', context)

def loginuser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('app')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Profiles.objects.get(username = username)
        except:
            messages.error(request, "User Not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is incorrect")
    context = {'page':page}
    return render(request, 'users/login_register.html', context)

def logoutuser(request):
    logout(request)
    messages.success(request, "User logged out!")
    return redirect('login')

    return render(request, 'users/login_register.html')
def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User Registered Successfully.")
            login(request, user)
    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)


def accounts(request):
    context = {}
    return render(request, 'users/account.html', context)