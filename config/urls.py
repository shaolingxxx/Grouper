"""Grouper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import fishes
from applications.fishes import urls as fish_url
from applications.users import urls as user_url

urlpatterns = [
    # url(r'^fishes/', fishes.site.urls),
    url(r'^fishes/', include(fish_url, namespace="fishes")),
    url(r'^account/', include(user_url, namespace="users")),
]
