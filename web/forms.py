from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
    
    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            return valid
        
        question_text = self.cleaned_data.get('text')
        conditions = [
            len(question_text.split()) >= 1,
            len(question_text) >= 5,
            question_text.endswith('?')
        ]
        
        if all(conditions):
            return True
        else:
            self.add_error('text', 'Вопрос должен содержать минимум одно слово, пять символов и заканчиваться вопросительным знаком.')
            return False