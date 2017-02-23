from django.conf.urls import url
from account import views



urlpatterns = [
    url(r'^home/$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),

    url(r'^index/$', views.index, name='index'),

    # url(r'$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
]
