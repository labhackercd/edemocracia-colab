
from django.conf.urls import patterns, url

from .views import {{ app_name_camel }}ProxyView

urlpatterns = patterns('',
    url(r'^(?P<path>.*)$', GitlabProxyView.as_view(), name='{{ app_name }}'),
)
