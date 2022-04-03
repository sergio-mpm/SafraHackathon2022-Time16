"""OpenBankingExpansion URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Tela_2/tela2.html', views.Tela_2, name='Tela_2/tela2'),
    path('Tela_3/tela3.html', views.Tela_3, name='Tela_3/tela3'),
    path('Tela_4/tela4.html', views.Tela_4, name='Tela_4'),
    path('Tela_5/tela5.html', views.Tela_5, name='Tela_5'),
    path('Tela_6/tela6.html', views.Tela_6, name='Tela_6'),
    path('admin/', admin.site.urls),
]
