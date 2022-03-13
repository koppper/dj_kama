from django.urls import path

from .views import *


urlpatterns = [
    path('', blog_get, name='blog'),
    path('cat/<str:slug>', get_category, name='category')
]
