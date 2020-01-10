from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('rooms', api.rooms),
    url('say', api.say),
    url('pick-up', api.pick_up),
    url('drop', api.drop),
    url('eat', api.eat),
    url('items', api.items)
]