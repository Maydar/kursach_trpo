from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="Автор статьи")
    publish_date = models.DateTimeField("Дата публикации")
    text = models.TextField("Текст статьи")
    title = models.CharField("Заголовок", max_length=255)
    image = models.ImageField("Изображение статьи", upload_to='img')