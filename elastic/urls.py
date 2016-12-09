from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.IndexPageView.as_view(), name='index'),
        url(r'^search_data/?$', views.searchData.as_view(), name='search_data'),
        ]
