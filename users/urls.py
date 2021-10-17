from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.loginuser, name='login' ),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.profiles , name='profiles'),
    path('single_profile/<str:pk>/', views.single_profile, name='single_profile'),
    path('resgister/', views.registeruser, name='register'),
    path('accounts/', views.accounts, name='account')
]