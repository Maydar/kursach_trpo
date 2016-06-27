from core.base import BaseRecord


class TestRecord(BaseRecord):
    TABLE_NAME = 'core_test'
    FIELDS = {
        'id',
        'user_id',
        'title',
        'creation_date',
        'description',
        'total_points'
    }


class QuestionRecord(BaseRecord):
    TABLE_NAME = 'core_question',
    FIELDS = {
        'id',
        'test_id',
        'title',
    }


class AnswerRecord(BaseRecord):
    TABLE_NAME = 'core_answer',
    FIELDS = {
        'id',
        'test_id',
        'user_id',
        'question_id'
        'answer_variant_id'
    }