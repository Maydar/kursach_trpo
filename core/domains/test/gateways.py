from core.domains.test.models import Test, TestResult
from core.gateway import Gateway


class TestGateway(Gateway):
    TABLE_NAME = 'core_test'
    FIELDS = {
        'id',
        'user_id',
        'title',
        'creation_date',
        'description',
        'total_points'
    }


class TestResultGateway(Gateway):
    TABLE_NAME = 'core_testresult',
    FIELDS = {
        'id',
        'test_id',
        'user_id',
        'points'
    }