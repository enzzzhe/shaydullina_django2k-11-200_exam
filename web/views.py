from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Question
from .forms import QuestionForm
import random

def index(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.answer = random.choice(['ДА', 'НЕТ'])
            question.save()
            return redirect('answer:answer', question_id=question.id)
    else:
        form = QuestionForm()

    return render(request, 'index.html', {'form': form})

def answer(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return HttpResponseNotFound("Вопрос не найден")
        
    return render(request, 'answer.html', {'question': question})
