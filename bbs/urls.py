from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('write_post/', views.PostWrite.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    # IP주소/bbs/category/slug/
    path('category/<str:slug>/', views.category_list),
    
    path('login/signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
