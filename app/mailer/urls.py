# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from mailer.views import IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', cache_page(60*15)(IndexView.as_view()), name="index"),
]
