from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from core.domains.article.models import Article
from core.domains.question.models import Question, Answer, TextQuestion, AudioQuestion
from core.domains.test.models import Test, TestResult


class TestAdmin(ModelAdmin):
    list_display = ('title', 'creation_date')


class TestResultAdmin(ModelAdmin):
    list_display = ('id','user', 'test')

admin.site.register(Test, TestAdmin)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(TextQuestion)
admin.site.register(AudioQuestion)
admin.site.register(Answer)