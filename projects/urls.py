from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello, name='app'),
    path('prject_details/<str:pk>/', views.saybye, name='viewapp'),
    path('project-form/', views.createform, name='project-form' ),
    path('updateform/<str:pk>/', views.updateform, name='updateform'),
    path('deleteproject/<str:pk>/',  views.deletetemplate, name='deleteproject'),
]