from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^!(?P<url_hash>[a-zA-Z0-9]+)$', views.InfoView.as_view(),
        name='url_info'),
    url(r'^(?P<url_hash>[a-zA-Z0-9]+)$', views.RedirectView.as_view(),
        name='redirect'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
