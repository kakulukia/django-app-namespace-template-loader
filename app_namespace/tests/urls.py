"""Urls for testing app_namespace"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='template.html'),
        name='template-view'),
    url(r'^admin/', include(admin.site.urls)),
]
