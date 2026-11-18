from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')

def index(request):
    return HttpResponse("Главная страница каталога LocalLibrary")
