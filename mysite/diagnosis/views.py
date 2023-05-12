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


def curves(request):
    return render(request, "diagnosis/layout.html")


def model_evaluation(request):
    return render(request, "diagnosis/layout.html")


def aboutus(request):
    return render(request, "diagnosis/layout.html")