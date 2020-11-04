from django.urls import path
from rest_framework.routers import DefaultRouter

# Views
from app.main import viewsets

urlpatterns = [
    path("", viewsets.JudgmentCreate.as_view()),
]
