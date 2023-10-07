from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the quickstar_first_steps index.")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def update_profile(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        bio = request.POST.get("bio")
        birthday_date = request.POST.get("birthday_date")

        # Ensure the username or email isn't taken by other users (excluding the current user)
        if (
            CustomUser.objects.exclude(pk=request.user.pk)
            .filter(username=username)
            .exists()
        ):
            messages.error(request, "Username is already in use.")
            return redirect("profile")

        if CustomUser.objects.exclude(pk=request.user.pk).filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("profile")

        request.user.username = username
        request.user.email = email
        request.user.bio = bio
        request.user.birthday_date = birthday_date
        request.user.save()

        messages.success(request, "Profile updated successfully")
        return redirect("profile")

    return render(request, "profile.html", {"user": request.user})
