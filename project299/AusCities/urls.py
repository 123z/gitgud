from django.conf.urls import url
from . import views

app_name = 'auscities'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^result/$', views.result, name='result'),
    url(r'^about/$', views.about, name='about'),
    url(r'^help/$', views.help, name='help'),
	url(r'^location/(?P<id>\d+)/$', views.location, name='location'),
	url(r'^profile/$', views.result, name='profile'),
    ]