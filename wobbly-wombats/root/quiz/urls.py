from .views import create_quiz
from django.urls import path


urlpatterns = [
    path('quiz/<str:category>', create_quiz)
]
