from django.urls import path
from . import views
urlpatterns = [
    path('images/', views.Images, name= 'images'),
    path('', views.Feed, name= 'feed')
]
