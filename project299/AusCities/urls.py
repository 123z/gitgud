from django.conf.urls import url
from . import views

app_name = 'auscities'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^result/$', views.searched, name='result'),
    url(r'^about/$', views.about, name='about'),
    url(r'^help/$', views.help, name='help'),
    url(r'^result/Student/$', views.Student, name='Student'),
    url(r'^result/Tourist/$', views.Tourist, name='Tourist'),
    url(r'^result/Businessman/$', views.Businessman, name='Businessman'),
	url(r'^location/(?P<id>\d+)/$', views.location, name='location'),
	url(r'^profile/$', views.result, name='profile'),
	url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/create$', views.createadmin, name='createadmin'),
    url(r'^user/$', views.user, name='user'),
    url(r'^admin/add_info/$', views.info, name='info'),
    ]
