from django.conf.urls import include, url
from cloneapp.views import *
from django.contrib import admin
# from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^create_listing/$', login_required(ListingCreateView.as_view()), name='listing_create_view'),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url(r'^accounts/profile/$', login_required(ProfileUpdateView.as_view()), name="profile_update_view"),
    # url(r'^accounts/profile/listings/$', login_required(ProfileListView.as_view()), name='profile_list_view'),
    # url(r'^listing/(?P<pk>\d+)/delete/$', login_required(ListingDeleteView.as_view()), name="listing_delete_view"),
    # url(r'^listing/(?P<pk>\d+)/update/$', login_required(ListingUpdateView.as_view()), name='listing_update_view'),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^region_list/$', RegionListView.as_view(), name='region_list_view'),
    url(r'^category/(?P<pk>\d+)/thumbnail/$', CategoryListThumbnailView.as_view(), name='category_list_thumbnail_view'),
    url(r'^city_list/(?P<pk>\w+)/thumbnail/$', CityListThumbnailView.as_view(), name='city_list_thumbnail_view'),
    url(r'^category/(?P<pk>\d+)/gallery/$', CategoryListGalleryView.as_view(), name='category_list_gallery_view'),
    url(r'^city_list/(?P<pk>\w+)/gallery/$', CityListGalleryView.as_view(), name='city_list_gallery_view'),
    url(r'^category/(?P<pk>\d+)/list/$', CategoryListListView.as_view(), name='category_list_list_view'),
    url(r'^city_list/(?P<pk>\w+)/list/$', CityListListView.as_view(), name='city_list_list_view'),
]
