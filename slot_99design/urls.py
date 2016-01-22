from django.conf.urls import include, url
from django.contrib import admin
from contests import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^contest/(?P<id>\d+)/', views.contest_detail, name='contest_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
