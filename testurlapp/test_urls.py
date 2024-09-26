from django.urls import re_path
from testurlapp import views

urlpatterns = [
    re_path(r'user/(?P<month>\d{2})/(?P<year>\d{4})/', views.home, name="home"),
]
