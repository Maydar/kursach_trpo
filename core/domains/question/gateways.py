from core.base import Connection
from core.domains.question.models import TextQuestion, AudioQuestion, Answer



class AnswerGateway:
    # TABLE_NAME = 'core_answer'
    # FIELDS = {
    #     'id'
    #     'question_id',
    #     'user_id',
    #     'test_id',
    #     'answer_variant_id'
    # }

    @staticmethod
    def get_answers(user_id, test_id):
        return Answer.objects.raw("""SELECT * FROM {0} WHERE user_id = '{1}'
                                    AND test_id = '{2}'""".format('core_answer', user_id, test_id))

    @staticmethod
    def insert_answer(question_id, user_id, test_id, answer_variant_id):
        connection = Connection.get_connection()
        c = connection.cursor()
        columns = ['question_id', 'user_id', 'test_id', 'answer_variant_id']
        c.execute("""
            INSERT INTO {} ({}) VALUES ({})
        """.format('core_answer', columns, [question_id, user_id, test_id, answer_variant_id]))
        connection.commit()


