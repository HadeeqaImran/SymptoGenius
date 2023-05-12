from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "diagnosis/home.html")


def navbar(request):
    return render(request, "diagnosis/navbar.html")


def footer(request):
    return render(request, "diagnosis/footer.html")


def layout(request):
    return render(request, "diagnosis/layout.html")