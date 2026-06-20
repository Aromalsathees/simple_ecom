from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout



def register_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        password = request.POST.get(
            "password"
        )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(
            "login"
        )

    return render(
        request,
        "accounts/register.html"
    )




def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "home"
            )

    return render(
        request,
        "accounts/login.html"
    )



def logout_view(request):

    logout(request)

    return redirect(
        "login"
    )