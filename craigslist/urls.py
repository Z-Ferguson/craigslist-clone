from django.conf.urls import url, include
from django.contrib import admin
# from cloneapp.views import IndexView
from django.contrib.auth import views as auth_views
from cloneapp.views import *



urlpatterns = [
    url(r'^cloneapp/', include('cloneapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/$', ProfileListView.as_view()),
    ]
