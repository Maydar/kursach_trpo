from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Пожалуйста введите корректный логин и пароль"
                           "Помните, что поля зависимы от регистра",
        'inactive': "Эта учетная запись неактивна",
    }