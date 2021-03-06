from django.conf.urls import url
from saidditApp import views

urlpatterns = [
    url('^$', views.homepage),
    url('^login/$', views.loginpage),
    url('^logout/$', views.logoutfunc),
    url('^post/(?P<postid>[0-9]+)/$', views.viewpostpage),
    url('^r/(?P<subsaidditname>\w+)/$', views.viewsubsaidditpage),
    url('^addpost/(?P<subsaidditname>.+)/$', views.addpostpage),
    url('^addcomment/(?P<postid>[0-9]+)/$', views.addcommentfunc),
    url('^register/$', views.registerpage)

]
