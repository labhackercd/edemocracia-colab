# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from tastypie.api import Api

from .models import (UserResource, MessageResource, RevisionResource,
                     TicketResource, WikiResource)
from .views import VoteView


api = Api(api_name='colab')
api.register(UserResource())
api.register(MessageResource())
api.register(RevisionResource())
api.register(TicketResource())
api.register(WikiResource())


urlpatterns = patterns('',
    url(r'message/(?P<msg_id>\d+)/vote$', VoteView.as_view()),

    # tastypie urls
    url(r'', include(api.urls)),
)
