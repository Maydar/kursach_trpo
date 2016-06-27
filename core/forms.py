from django.contrib.auth.forms import AuthenticationForm
from core.model.test.forms import *
from core.model.question.forms import *
from core.model.article.forms import *


class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Пожалуйста введите корректный логин и пароль"
                           "Помните, что поля зависимы от регистра",
        'inactive': "Эта учетная запись неактивна",
    }