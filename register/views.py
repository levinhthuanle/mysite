from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register (response):
    if response.method == "POST":
        form = RegisterForm(response.POST)    
        if form.is_valid():
            form.save()

        # Thêm comment để điều hướng và không tạo thêm user
        #return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})