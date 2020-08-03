from django.shortcuts import render
from django.views import generic

from .models import Quiz, Site
from .forms import QuizForm


def create_quiz(request, category=None):
    if request.method == 'GET':
        quiz = Quiz.objects.create(user=request.user, category=category)
        random_site = Site.objects.create(quiz=quiz)
        context = {random_site}

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            pass


