"""
URL configuration for social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from media_app import views 

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('posts/create/',views.PostCreate.as_view(),name='create'),
    path('users/',views.UserProfileList.as_view(),name='users'),
    path('users/create/',views.UserProfileCreate.as_view(),name='user_create'),
    path('',views.UserProfileLogin.as_view(),name='login'),
    path('users/filter/',views.UserProfileFilter.as_view(),name='filter'),
    path('users/update/<int:pk>',views.UserProfileUpdate.as_view(),name='user_update'),
    path('users/delete/<int:pk>',views.UserProfileDelete.as_view(),name='user_delete'),
    path('logout/', LogoutView.as_view(),name='logout'),
]













