from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('<int:pk>/', views.PostView.as_view()),
    path('write_post/', views.PostWrite.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    # IP주소/bbs/category/slug/
    path('category/<str:slug>/', views.category_list),
    
    #path('signup/', views.SignUp.as_view()),
    #path('login/', views.LogIn.as_view()),
]
