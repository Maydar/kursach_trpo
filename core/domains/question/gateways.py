from core.domains.question.models import TextQuestion, AudioQuestion, Answer
from core.gateway import Gateway


class TextQuestionGateway(Gateway):
    TABLE_NAME = 'core_textquestion'
    FIELDS = {
        'id',
        'title',
        'description'
    }


class AudioQuestionGateway(Gateway):
    TABLE_NAME = 'core_audioquestion'
    FIELDS = {
        'text',
        'audio_file'
    }


class AnswerQuestionGateway(Gateway):
    TABLE_NAME =  'core_answer'
    FIELDS = {
        'question_id',
        'user_id',
        'content'
    }