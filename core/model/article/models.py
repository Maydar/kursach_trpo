from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="Автор статьи")
    publish_date = models.DateTimeField("Дата публикации", default=timezone.now)
    text = models.TextField("Текст статьи")
    title = models.CharField("Заголовок", max_length=255)

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'