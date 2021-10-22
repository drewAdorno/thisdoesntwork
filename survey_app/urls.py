from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('write_post', views.write_post),
    path('process_post', views.process_post),
    path('clear', views.clear_session),
]