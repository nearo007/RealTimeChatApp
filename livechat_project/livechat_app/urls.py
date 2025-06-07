from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('<str:room_name>/get_messages/<str:room_id>', views.get_messages, name='get_messages'),
    path('get_available_rooms', views.get_available_rooms, name='get_available_rooms')
]