from django.conf.urls import url
from . import views

app_name = 'auscities'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register2/$', views.register2, name='register2'),
    ]