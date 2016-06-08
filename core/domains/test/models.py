
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# @brief deprecated
class Test(models.Model):
    user = models.ForeignKey(User, verbose_name="Автор теста")
    title = models.CharField("Название теста", max_length=255)
    creation_date = models.DateTimeField("Дата создания", default=timezone.now)
    description = models.TextField("Описание", default='')

    total_points = models.IntegerField("Макс. кол-во баллов", default=100)

    def get_total_points(self):
        return self.total_points

    def get_title(self):
        return self.title

    def get_creation_date(self):
        return self.creation_date

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"



class TestResult(models.Model):
    user = models.ForeignKey(User, verbose_name="Ученик")
    test = models.ForeignKey(Test, verbose_name="Тест")
    points = models.IntegerField("Оценка за тест", default=0)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
