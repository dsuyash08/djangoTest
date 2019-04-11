from django.urls import path
from . import  views

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('subjects/<int:pk>/', views.subjects_detail, name='subjects_detail'),
]