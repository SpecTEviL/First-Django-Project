from django.urls import path
from . import views         # the . specifies the current folder

urlpatterns = [
    path('', views.home)
]
