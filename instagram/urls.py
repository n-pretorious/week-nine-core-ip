from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('',views.profile, name = 'profile'),
    # path('post', views.comment, name= 'postComment')
]