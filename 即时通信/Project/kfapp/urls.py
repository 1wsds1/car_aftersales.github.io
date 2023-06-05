#from django.urls import path
#from . import views
 
#urlpatterns = [
#    path('', views.index, name='index'),
#    path(r'^(?P<room_name>[^/]+)/$', views.room, name='room')
#]

#from django.conf.urls import url

#from . import views

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
#]

from django.urls import path
from django.conf.urls import url
from . import consumers
from . import views


websocket_urlpatterns = [
    url(r'^ws/kfapp/room(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('', views.QA, name='QA'),
    path('tb.html/', views.tb, name='tb'),
    path('<str:room_name>/', views.room, name='room'),
]
