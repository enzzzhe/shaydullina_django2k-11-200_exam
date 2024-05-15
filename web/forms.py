from django import forms
from web.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question")