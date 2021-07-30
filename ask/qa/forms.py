from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def save(self):
        user = User.objects.get(username='Nikk')
        question = Question(author=user, **self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def save(self, question):
        user = User.objects.get(username='Nikk')
        answer = Answer(author=user, question=question, **self.cleaned_data)
        answer.save()
        return answer
