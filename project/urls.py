from django.conf.urls import patterns, url

from django.shortcuts import render

urlpatterns = patterns('',
    url(r'^$', render, {
        'template_name': 'index.html',
        'dictionary': {'list': [1,2,2,3]}
        }),
)
