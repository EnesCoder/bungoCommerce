from django.urls import path
from . import views

app_name = "authent"
urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("createuser", views.createuser, name="createuser"),
    path("loginuser", views.loginuser, name="loginuser"),
]
