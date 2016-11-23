from django.conf.urls import url
# from . import views
from cloneapp.views import IndexView
# import cloneapp

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
]
