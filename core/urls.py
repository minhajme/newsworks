"""stratfeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView
from webapp.views import CustomizedAdminLoginView, logout, UserProfileView, DashboardView, ListIndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/', RedirectView.as_view(pattern_name='login')),
    path('accounts/profile/', UserProfileView.as_view(), name="profile"),

    path('login/', CustomizedAdminLoginView.as_view(), name='login'),
    path('logout', logout, name='logout'),

    path('', RedirectView.as_view(pattern_name='dashboard'), name="index"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('list/index/', ListIndexView.as_view(), name='list-index')
]
