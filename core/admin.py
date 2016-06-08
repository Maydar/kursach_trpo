from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from core.domains.article.models import Article
from core.domains.question.models import Question, Answer, TextQuestion, AudioQuestion, AnswerVariant
from core.domains.test.models import Test, TestResult


class TestAdmin(ModelAdmin):
    list_display = ('title', 'creation_date')


class TestResultAdmin(ModelAdmin):
    list_display = ('id','user', 'test')


class AnswerVariantInline(admin.TabularInline):
    model = AnswerVariant
    extra = 0

class QuestionAdmin(ModelAdmin):
    inlines = (AnswerVariantInline,)

admin.site.register(Test, TestAdmin)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(TextQuestion, QuestionAdmin)
admin.site.register(AudioQuestion, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(AnswerVariant)