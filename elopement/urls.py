from django.conf.urls import url
from . import views

app_name = "elopement"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'rsvp/$', views.rsvp, name="rsvp"),
    url(r'rsvp/search', views.search_invitees, name="search_invitees")
]
