from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage),
    path('profile/', views.profile),
]
