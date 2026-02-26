from django.urls import path
from . import views

#url patterns for the playground app

urlpatterns = [
    path('hello/', views.index)
]