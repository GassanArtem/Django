from django.shortcuts import render
from django.http import HttpResponse

# def index_page(request):
#     return render(request, 'index.html')

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
