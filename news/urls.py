from django.urls import path
from . import views

urlpatterns = [
    path('bot/', views.NewsBotView.as_view()),
]
