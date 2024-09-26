"""
URL configuration for my_first_project project.

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
from django.urls import path, include, re_path

from teststaticapp import views as test_views
from hello import views as hello_views
from validformapp import views as form_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_app/', include('testurlapp.test_urls')),
    path('index/', test_views.home, name="index"),
    path('', hello_views.home, name="home"),
    re_path(r'(?P<dog_id>\d+)/', hello_views.dog_detail, name="dog_page"),
    path('formpage/', form_views.form_page, name="form_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
