from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib import admin

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name = 'story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<int:pk>/update/', views.StoryUpdate.as_view(), name='StoryUpdate'),
    path('<int:pk>/delete/', views.StoryDelete.as_view(), name='StoryDelete'),
]
