from django.conf.urls import  patterns,include, url
from django.contrib import admin
from user_mgmt import settings
from account.views import *


print("*********url************")
urlpatterns = patterns('',
    url(r'^registration/$', register, name='register'),
    url(r'^login_views/$', login_views, name='login_views'),
    url(r'^home/$', home, name='home'),
    #url(r'^logout/$', account_logout, name='logout'),
    url(r'^logout_views/$',logout_views, name='logout_views'), 
    url(r'^$',login_views, name='login'), 
)

