'''Routes file'''

from django.http import HttpResponse

def index(request):
    '''Home products page'''
    return HttpResponse("<h1>Products home page<h1>")

def products(request, id = 0):
    '''products'''
    return HttpResponse(f"Product {id}")

def reviews(request, id = 0):
    '''reviews'''
    return HttpResponse(f"Reviews {id}")
