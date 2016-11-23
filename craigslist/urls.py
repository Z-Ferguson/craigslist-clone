from django.conf.urls import url, include
from django.contrib import admin
# from cloneapp.views import IndexView


urlpatterns = [
    url(r'^cloneapp/', include('cloneapp.urls')),
    url(r'^admin/', admin.site.urls),
    ]
