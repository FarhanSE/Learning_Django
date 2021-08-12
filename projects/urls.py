from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello, name='hello'),
    path('bye/<int:pk>/', views.saybye, name='bye')
]