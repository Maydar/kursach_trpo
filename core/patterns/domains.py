from django.contrib.auth.models import User


class StudentDomain:

    @staticmethod
    def get_all_students():
        return User.objects.filter(groups__name__in=['student']).all()


class TestDomain:
    @staticmethod
    def create_test():
        pass


    @staticmethod
    def change_test():
        pass


    @staticmethod
    def get_all_tests():
        pass


    @staticmethod
    def remove_test():
        pass

class QuestionDomain:
    @staticmethod
    def create_question():
        pass

    @staticmethod
    def change_question():
        pass

    @staticmethod
    def get_all_questions():
        pass

    @staticmethod
    def remove_question():
        pass

class AnswerDomain:
    @staticmethod
    def create_answer():
        pass

    @staticmethod
    def get_answers():
        pass