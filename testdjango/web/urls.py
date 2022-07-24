"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from .views import register_view, main_view, login_view, logout_view, SiteView, SiteDetailView, SiteUpdateView, \
    SiteListView

urlpatterns = [
    path('', main_view, name='main'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('sites/add/', SiteView.as_view(), name='site-add'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site'),
    path('sites/<int:pk>/edit/', SiteUpdateView.as_view(), name='site-edit'),
    path('sites/', SiteListView.as_view(), name='site-list'),
]
