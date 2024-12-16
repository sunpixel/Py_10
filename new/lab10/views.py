"""
Module docstring
"""

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse

# Also possible to use this reponse classes to send status codes HttpBadRequest, Http404,
# HttpResponseServerError, etc...

def index(request):
    '''Home page'''
    return HttpResponse("<h1>Home page<h1>")

def about(request, name="None", age=0):
    '''About page'''
    return HttpResponse(f"""
                        <h2>About<h2>
                        <body>
                            Name: {name},
                            Age: {age}
                        <body>
                        """)

def redirection(request):
    '''Redirecting to'''
    return HttpResponseRedirect("/404")

def perma_redirection(request):
    '''Redirecting to'''
    return HttpResponsePermanentRedirect("/404")

def error(request):
    '''404 view'''
    return HttpResponse('<h1>404<h1>')

def jresponse(request):
    '''sends JSON response'''
    age = request.GET.get('age')
    name = request.GET.get('name')
    username = request.GET.get('username')
    json = {
        'name' : name,
        'age' : age,
        'username' : username
    }
    return JsonResponse(json)

def cookie(request):
    '''Sets a cookie'''
    name = request.GET.get('name')
    resp = HttpResponse(f'<h1>Hey there {name}<h1>')
    resp.set_cookie("username", name)
    return resp

def show_cookie(request):
    '''Gets all availiable cooks'''
    cookies = request.COOKIES
    return JsonResponse({'cookies': cookies})
