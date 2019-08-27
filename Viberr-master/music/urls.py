from django.conf.urls import url

from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^vocabularys/(?P<filter_by>[a-zA_Z]+)/$', views.vocabularys, name='vocabularys'),
    url(r'^(?P<topic_id>[0-9]+)/e2vn/(?P<type_compare>[0-9]+)$', views.compare_vocabualry, name='compare_word'),
    url(r'^create_topic/$', views.create_topic, name='create_topic'),
    url(r'^(?P<topic_id>[0-9]+)/create_vocabulary/$', views.create_vocabulary, name='create_vocabulary'),
    url(r'^(?P<topic_id>[0-9]+)/delete_vocabulary/(?P<vocabulary_id>[0-9]+)/(?P<local_delete>[0-9]+)$',
        views.delete_vocabulary,
        name='delete_vocabulary'),
    url(r'^(?P<topic_id>[0-9]+)/delete_topic/$', views.delete_topic, name='delete_topic'),
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

]
