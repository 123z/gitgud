from django.conf.urls import url
from AusCities import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
]
