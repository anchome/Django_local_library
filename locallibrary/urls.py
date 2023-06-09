"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# Use include() to add paths from the catalog application
from django.urls import path, include
# Añadir mapas URL para redirigir la URL base a nuestra aplicación
from django.views.generic import RedirectView
from django.conf import settings
# Use static() para añadir mapeo url para servir archivos estáticos durante el desarrollo (sólo)
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += [
    #path('', auth_views.LoginView.as_view(), name="login"),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
