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
    path("curves/", views.curves, name="curves"),
    path("model_evaluation/", views.model_evaluation, name="model_evaluation"),
    path("aboutus/", views.aboutus, name="aboutus"),
]