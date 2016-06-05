from django.forms import ModelForm

from core.domains.question.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']