from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from wagtailcomments_xtd import views


urlpatterns = [
    url(r'^$', views.pages, name='wagtailcomments_xtd_pages'),
    url(r'^(?P<pk>\d+)/$', views.comments, name='wagtailcomments_xtd_comments'),
    url(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/thread/$',
        views.comment_thread, name='wagtailcomments_xtd_comment_thread'),
    url(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/update/(?P<action>publish|unpublish|hide|show)/$',
        views.update, name='wagtailcomments_xtd_publication'),
]
