"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from lab10 import views
from hello import views as v2

product_patterns = [
    path('', v2.index),
    path('reviews', v2.reviews)
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/<str:name>/<int:age>', views.about),
    path('redirect', views.redirection),
    path('404', views.error),
    re_path(r'^redirect/perma', views.perma_redirection),
    re_path(r'^redirect', views.redirection),
    re_path(r'^jsresponse/', views.jresponse),
    re_path(r'^cookie/show', views.show_cookie),
    re_path(r'^cookie', views.cookie),
    path('products/<int:id>', include(product_patterns))
]
