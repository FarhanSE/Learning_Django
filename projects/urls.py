from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello, name='hello'),
    path('bye/<str:pk>/', views.saybye, name='bye'),
    path('project-form/', views.createform, name='project-form' ),
    path('updateform/<str:pk>/', views.updateform, name='updateform'),
    path('deleteproject/<str:pk>/',  views.deletetemplate, name='deleteproject'),
]