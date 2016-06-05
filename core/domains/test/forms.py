from django.forms import ModelForm, Form

from core.domains.test.models import Test


class TestCreateForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        test = super().save(commit=False)
        test.user = self.user
        test.save()

        return test