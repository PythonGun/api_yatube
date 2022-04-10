from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/posts/<int:pk>/', views.get_post), 
]