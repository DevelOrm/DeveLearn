from django.urls import path
from . import views

urlpatterns = [
    path('bot/', views.NewsBotView.as_view()),
    path('list/', views.NewsListView.as_view()),
    path('recent/', views.NewsRecentView.as_view()),
    path('search/', views.NewsSearchView.as_view()),
]
