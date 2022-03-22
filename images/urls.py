from django.urls import path
from . import views
urlpatterns = [
    path('images/', views.Images, name= 'images'),
    path('feed/', views.Feed, name= 'feed')
]
