from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns=[
    url(r'^home/', views.home, name='home'),
    url(r'^another/', views.another, name='another'),
    url(r'^third/', views.third, name='third'),
    url(r'^json_response/', views.json_response, name='json_response'),
    url(r'^jquery_test', views.jquery_test, name='jquery_test'),

    # class based views
    url(r'^view/', views.MyView.as_view()),
    url(r'^view/sub/', views.MorningGreetingView.as_view()),
    url(r'^form/', views.MyFormView.as_view()),
    url(r'^success/', views.SuccessView.as_view()),

    # serializer based views
    url(r'^list/', views.LionList.as_view()),
    url(r'crud/(?P<pk>[0-9]+)$', views.LionDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)