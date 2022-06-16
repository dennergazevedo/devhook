"""devhook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api import viewsets as usersviewsets
from posts.api import viewsets as postsviewsets

route = routers.DefaultRouter()

route.register('users', usersviewsets.UsersViewSet, basename="Users")
route.register('feeds', postsviewsets.FeedsViewSet, basename="Feeds")
route.register('stories', postsviewsets.StoriesViewSet, basename="Stories")
route.register('comments', postsviewsets.CommentsViewSet, basename="Comments")
route.register('interactions', postsviewsets.InteractionsViewSet, basename="Interactions")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include(route.urls)),
]
