from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles , name='profiles'),
    path('single_profile/<str:pk>/', views.single_profile, name='single_profile')
]