from django.forms import ModelForm

from core.domains.question.models import Question, TextQuestion


class TextQuestionForm(ModelForm):
    class Meta:
        model = TextQuestion
        fields = ['title', 'text']