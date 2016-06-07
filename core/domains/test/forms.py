import json

from django.forms import ModelForm, Form, forms

from core.domains.question.forms import  TextQuestionForm
from core.domains.question.models import Question, TextQuestion
from core.domains.test.models import Test
from core.base import BaseFormSet


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


class TestEditForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']


class CreateTestForm(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__()
        data = kwargs.get('data', {})

        if data:
            self.test = TestEditForm(json.loads(data.get('test', "{}")))
            self.questions = {}
            if 'questions' in data:
                question_set = json.loads(data.get('questions'))

                if question_set['hidden-question']:
                    del question_set['hidden-question']

                forms_id = map(lambda x: x.split('_')[1], question_set.keys())

                for form_id, form_data in question_set.items:
                    id = form_id.split('_')[1]
                    self.questions[form_id] = TextQuestionForm(form_data)
        else:
            self.test = TestEditForm()
            self.question_hidden = TextQuestionForm()
            self.question_0 = TextQuestionForm()

    def is_valid(self):
        result = True
        if not self.test.is_valid():
            result = False
            self.errors['test'] = self.test.errors

        if not self._is_valid_set(self.questions, 'questions'):
            result = False
            self.errors['questions'] = self.questions.errors

        return result

    def save(self):
        for value in self.questions.values():
            question = value.save(commit=False)
            question.test = self.test.instance
            question.save()
            value.save_m2m()

        if self.test.has_changed():
            test = self.test.save()
        else:
            test = self.test.instance

        return test


class EditTestForm(BaseFormSet):

    def __init__(self, *args, **kwargs):
        super().__init__()
        data = kwargs.get('data', {})
        user = kwargs.get('user', {})
        test_instance = kwargs.get('test_instance', {})

        question_instances = TextQuestion.objects.filter(test=test_instance).all()

        if data:
            self.test = TestEditForm(json.loads(data.get('test', "{}")), instance=test_instance)
            self.questions = {}

            if 'questions' in data:
                question_set = json.loads(data.get('questions'))

                if question_set['hidden-question']:
                    del question_set['hidden-question']

                forms_id = map(lambda x: x.split('_')[1], question_set.keys())

                for question_instance in question_instances:
                    if str(question_instance.id) not in forms_id:
                        question_instance.delete()

                for form_id, form_data in question_set.items:
                    id = form_id.split('_')[1]

                    if question_instances.filter(pk=id).exists():
                        instance = question_instances.get(pk=id)
                        self.questions[form_id] = TextQuestionForm(form_data, instance=instance)
                    else:
                        self.questions[form_id] = TextQuestionForm(form_data)

        else:
            self.test = TestEditForm(instance=test_instance)
            self.questions = {}

            for question_instance in question_instances:
                self.questions['question_' + str(question_instance.id)] = \
                    TextQuestionForm(instance=question_instance)

            self.question_hidden = TextQuestionForm()
            self.question_0 = TextQuestionForm()

    def is_valid(self):
        result = True
        if not self.test.is_valid():
            result = False
            self.errors['test'] = self.test.errors

        if not self._is_valid_set(self.questions, 'questions'):
            result = False
            self.errors['questions'] = self.questions.errors

        return result

    def save(self):
        for value in self.questions.values():
            question = value.save(commit=False)
            question.test = self.test.instance
            question.save()
            value.save_m2m()

        if self.test.has_changed():
            test = self.test.save()
        else:
            test = self.test.instance

        return test