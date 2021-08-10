from django.urls import path
from . import views
urlpatterns = [
    path('hello/<str:pk>', views.hello, name='hello'),
    path('bye/', views.saybye, name='bye')
]