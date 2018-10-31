from django.conf.urls import url
from newsocial_app import views

urlpatterns = [
 url(r'^rol/$', views.RolList.as_view()),
 url(r'^rol/(?P<pk>[0-9]+)/$', views.RolDetail.as_view()),
]