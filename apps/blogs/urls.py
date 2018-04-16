from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^new', views.new),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^create', views.create),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^(?P<number>\d+)$', views.show),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^(?P<number>\d+)/edit$', views.edit),    # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^(?P<number>\d+)/delete$', views.destroy),    # This line has changed! Notice that urlpatterns is a list, the comma is in
                                # url(r'^test', views.test),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon
print('blogs.urls')
