from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, MyContactForm
from users.models import Profile


# Create your views here.
def index(request):
    context_dict = {}

    return render(request, 'users/index.html', context_dict)


def register(request):
    context_dict = {}

    if request.method == "GET":
        form = CustomUserCreationForm()

        context_dict["form"] = form
        return render(request, 'registration/register.html', context_dict)
    
    elif request.method == "POST":
        newly_register_user = CustomUserCreationForm(request.POST)

        if newly_register_user.is_valid():
            user = newly_register_user.save()
            login(request, user)

            return render(request, 'users/index.html')
        elif newly_register_user.errors:
            context_dict["form"] = CustomUserCreationForm()

            return render(request, 'registration/register.html', context_dict)



@login_required
def profile(request, username):
    context_dict = {}

    user_inatnce = User.objects.get(username=username)
    profile_details = Profile.objects.get(user_id=user_inatnce.id)
    context_dict["profile_details"] = profile_details
    context_dict["user_inatnce"] = user_inatnce

    return render(request, 'users/profile.html', context_dict)
    


