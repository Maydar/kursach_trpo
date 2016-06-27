import json

from django.core.exceptions import PermissionDenied
from django.forms import ModelForm, Form

from core.model.article.models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        article = super().save(commit=False)
        article.user = self.user
        article.save()
        return article


class ArticleEditForm(Form):
    class Meta:
        model = Article
        fields = ['title', 'text']