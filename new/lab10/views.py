"""
Module docstring
"""

from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h1>Home page<h1>")
 
def about(request, name, age):
    return HttpResponse(f"""
                        <h2>About<h2>
                        <body>
                            Name: {name},
                            Age: {age}
                        <body>
                        """)
 
def contact(request):
    return HttpResponse("<h2>Contacts<h2>")
