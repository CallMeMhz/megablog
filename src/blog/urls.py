from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new', views.add_post_form, name='add'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_view, name='post'),
]
