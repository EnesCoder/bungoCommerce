from django.core.exceptions import ValidationError
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "authent/index.html")


def User_unique(username):
    return not User.objects.filter(username=username).exists()


def Return_to_index_with_err(err, request):
    return render(request, "authent/index.html", {
        "err": err,
    })


def createuser(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if len(username) <= 8 or len(password) <= 8:
        Return_to_index_with_err(
            "User name or password too short, please be sure they are longer than 8 characters", request)
    if User_unique(username):
        try:
            new_user = User.objects.create_user(
                username=username, password=password)
            new_user.save()

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
            else:
                Return_to_index_with_err(
                    "Could not authenticate user", request)

            print(request.POST)
            return HttpResponseRedirect(reverse("commerce:index"))
        except ValidationError as e:
            print(f"ValidationError: {e}")
            Return_to_index_with_err(
                "Could not validate user, please try again", request)
    else:
        Return_to_index_with_err("A user by that name already exists", request)


def signin(request):
    return render(request, "authent/login.html")


def loginuser(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("commerce:index"))
    else:
        return render(request, "authent/login.html", {
            "err": "Could not authenticate user"
        })
