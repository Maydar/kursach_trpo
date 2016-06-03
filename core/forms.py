from django.contrib.auth.forms import AuthenticationForm
from core.domains.test.forms import *
from core.domains.question.forms import *
from core.domains.article.forms import *


class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Пожалуйста введите корректный логин и пароль"
                           "Помните, что поля зависимы от регистра",
        'inactive': "Эта учетная запись неактивна",
    }