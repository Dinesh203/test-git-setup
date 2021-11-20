from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("user_login/", views.user_login, name="loginpage"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="user_profile"),
]
