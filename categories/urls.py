
from django.urls import path
from .views import *
urlpatterns = [
  path('add/', add_category,name='add_category'),
]
