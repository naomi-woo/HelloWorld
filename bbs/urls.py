from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create_post/', views.PostCreate.as_view()),

    path('login/signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
