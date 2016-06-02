from core.domains.question.models import TextQuestion, AudioQuestion, Answer


class TextQuestionGateway(object):
    def insert(self):
        return TextQuestion.objects.raw("")

    def delete(self):
        return TextQuestion.objects.raw("")

    def get_all(self):
        return TextQuestion.objects.raw("")

    def find_by_test(self):
        return TextQuestion.objects.raw("")

    def update(self, object):
        return TextQuestion.objects.raw("")


class AudioQuestionGateway(object):
    def insert(self):
        return AudioQuestion.objects.raw("")

    def delete(self):
        return AudioQuestion.objects.raw("")

    def get_all(self):
        return AudioQuestion.objects.raw("")

    def find_by_test(self):
        return AudioQuestion.objects.raw("")

    def update(self, object):
        return AudioQuestion.objects.raw("")


class AnswerQuestionGateway(object):
    def insert(self):
        return Answer.objects.raw("")

    def delete(self):
        return Answer.objects.raw("")

    def get_all(self):
        return Answer.objects.raw("")

    def find_by_question(self):
        return Answer.objects.raw("")

    def update(self, object):
        return Answer.objects.raw("")