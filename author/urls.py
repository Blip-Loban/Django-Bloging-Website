
from django.urls import path
from .views import *
urlpatterns = [
  path('add/', add_author,name='add_author'),
]
