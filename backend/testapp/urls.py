"""
URL configuration for Diploma_Cracker_v1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('topper/', views.topper_view, name='topper'),
    path('coding/', views.coding_view, name='coding'),
    path('theory/', views.theory_view, name='theory'),
    path('timer/', views.timer_view, name='timer'),
    path('particular/<str:sub>', views.sub_detail, name='particular'),
]
