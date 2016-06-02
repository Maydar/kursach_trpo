from django.contrib.auth.models import User
from django.db import models

from core.domains.test.models import Test


class Question(models.Model):
    test = models.ForeignKey(Test, verbose_name="Тест")
    title = models.CharField("Заголовок вопроса", max_length=255)


class TextQuestion(Question):
    text = models.TextField("Текст вопроса")

    class Meta:
        verbose_name = "Текстовый вопрос"
        verbose_name_plural = "Текстовые вопросы"


class AudioQuestion(Question):
    text = models.TextField("Текст вопроса")
    audio_file = models.FileField("Аудио-файл", upload_to='audio')

    class Meta:
        verbose_name = "Аудио вопрос"
        verbose_name_plural = "Аудио вопросы"


class Answer(models.Model):
    user = models.ForeignKey(User, verbose_name="Ученик")
    question = models.ForeignKey(Question, verbose_name="Вопрос")
    content = models.TextField("Ответ")
