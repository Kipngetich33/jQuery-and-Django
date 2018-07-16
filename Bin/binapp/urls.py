from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^home/', views.home, name='home'),
    url(r'^another/', views.another, name='another'),
    url(r'^third/', views.third, name='third'),
    url(r'^json_response/', views.json_response, name='json_response'),
]