from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.main, name="index"),
    path('question/<int:question_id>/', views.answer, name='answer'),
]