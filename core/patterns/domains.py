from django.contrib.auth.models import User
from django.utils import timezone

from core.model.test.records import TestRecord, QuestionRecord, AnswerRecord


class StudentDomain:

    @staticmethod
    def get_all_students():
        return User.objects.filter(groups__name__in=['student']).all()


class TestDomain:
    test = None

    @classmethod
    def create_test(self, test_data=None):
        errors = self.validate(test_data)
        if self.test is None and not errors:
            test = TestRecord(user_id=test_data['user'],
                              title=test_data['title'],
                              creation_date=timezone.now,
                              description=test_data['description'],
                              total_points=100)

            test.save()
        else:
            return errors

    @classmethod
    def validate(self, test_data):
        errors = {}

        if not "title" in test_data:
           errors['title'] = {
               "message": "Обязательноe поле"
           }

        if not "description" in test_data:
            errors['description'] = {
                "message": "Обязательноe поле"
            }

        return errors

    @classmethod
    def change_test(self, test_data):
        errors = self.validate(test_data)
        if self.test is None and not errors:
            self.test = TestRecord(user_id=test_data['user'],
                              title=test_data['title'],
                              creation_date=timezone.now,
                              description=test_data['description'],
                              total_points=100)

            self.test.save()
        else:
            return errors

    @classmethod
    def get_all_tests(self, test):
        return self.test.all()

    @classmethod
    def remove_test(self):
        return self.test.delete()


class QuestionDomain:
    question = None

    @classmethod
    def create_question(self, question_data):
        errors = self.validate(question_data)

        if self.question is None and not errors:
            self.question = QuestionRecord(title=question_data['title'],
                              text=question_data['text'],
                              test_id=question_data['test'])

            self.question.save()
        else:
            return errors


    @classmethod
    def change_question(self, question_data):
        errors = self.validate(question_data)

        if not errors:
            self.question = QuestionRecord(title=question_data['title'],
                                           text=question_data['text'],
                                           test_id=question_data['test'])
            self.question.save()
        else:
            return errors


    @classmethod
    def validate(self, test_data):
        errors = {}

        if not "title" in test_data:
            errors['title'] = {
                "message": "Обязательноe поле"
            }

        if not "text" in test_data:
            errors['text'] = {
                "message": "Обязательноe поле"
            }

        return errors

    @classmethod
    def get_all_questions(self):
        return self.question.all()

    @classmethod
    def remove_question(self):
        return self.question.delete()


class AnswerDomain:
    asnwer = None

    @classmethod
    def create_answer(self, answer_data):
        self.question = AnswerRecord(user_id=answer_data['user'],
                                     test_id=answer_data['test'],
                                     question_id=answer_data['question'],
                                     answer_variant_id=answer_data['variant'])

        self.question.save()


    @classmethod
    def get_answers(self):
        return self.answer.all()