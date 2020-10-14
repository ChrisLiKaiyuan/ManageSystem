from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^create/$', CreateInfoView.as_view(), name='create_information'),
    re_path('^get/$', GetInfoListView.as_view(), name='get_information_list'),
    re_path('^search/$', SearchInfoView.as_view(), name='search_information'),
    re_path('^information/(?P<pk>\d+)/$', InfoView.as_view(), name='information'),
]
