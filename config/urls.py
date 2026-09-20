from django.contrib import admin

from django.urls import path

from core import views


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "donors/",
        views.donors,
        name="donors"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "request-blood/",
        views.request_blood,
        name="request_blood"
    ),

    path(
        "emergency/",
        views.emergency,
        name="emergency"
    ),
]
