from django.shortcuts import render
from django.http import HttpResponse
from django.http import *

# def index_page(request):
#     return render(request, 'index.html')

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id: {0} " \
                "Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)



#Блок возврата для ошибок сервера/клиента

#304 'Not Modifie'
def m304(request):
    return HttpResponseNotModified()

#400 'Bad Request'
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

#403 'Forbidden'
def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

#404 'Not Found'
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

#405 'Method is not allowed'
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

#410 'Content is no longer here'
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")

#500 'Something is wrong'
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")
