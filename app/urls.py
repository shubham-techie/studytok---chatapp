from django.urls import path
from . views import *

urlpatterns=[
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),

    path('', home, name='home'),
    path('room/<str:pk>/',room, name='room'),

    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),

    path('delete-message/<str:pk>', deleteMessage, name='delete-mssg'),

    path('update-user/', updateUser, name='update-user'),

    path('topics/', topicPage, name='topics'),
    path('activity/', activityPage, name='activity'),

]