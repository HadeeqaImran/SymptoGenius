from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("navbar/", views.navbar, name="navbar"),
    path("footer/", views.footer, name="footer"),
    path("layout/", views.layout, name="layout"),
]