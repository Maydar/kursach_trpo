from django.contrib.auth.models import User

from core.base import Connection
from core.domains.test.models import Test, TestResult



class TestResultGateway:
    TABLE_NAME = 'core_testresult',
    FIELDS = {
        'id',
        'test_id',
        'user_id',
        'points'
    }

    @staticmethod
    def get_results_by_user_id(self, user_id):
        return TestResult.objects.raw("SELECT * FROM {0} WHERE user_id = '{1}'".format('core_testresult', user_id))

    @staticmethod
    def get_results_by_test_id(self, test_id):
        return TestResult.objects.raw("SELECT * FROM {0} WHERE test_id = '{1}'".format('core_testresult', test_id))

    @staticmethod
    def get_results_by_username(self, username):
        user_id = User.objects.raw("SELECT id FROM {0} WHERE username = '{1}'".format('auth_user', username))
        return self.get_results_by_user_id(user_id)

    @staticmethod
    def get_results_by_testname(self, testname):
        test_ids = User.objects.raw("SELECT id FROM {0} WHERE title = '{1}'".format('core_test', testname))
        return self.get_results_by_test_id(test_ids[0])


class UserGateway:

    @staticmethod
    def get_students_by_name(username):
        return User.objects.raw("SELECT * FROM {0} WHERE username = '{1}'".format('auth_user', username))

    @staticmethod
    def get_all_students():
        c = Connection.get_connection().cursor()

        return User.objects.raw("""SELECT auth_user.id, auth_user.password, auth_user.last_login,
                                          auth_user.is_superuser, auth_user.first_name, auth_user.last_name,
                                          auth_user.email, auth_user.is_staff,
                                          auth_user.is_active, auth_user.date_joined, auth_user.username
                                   FROM {0}
                                   LEFT JOIN {1} ON auth_user_groups.group_id = auth_group.id
                                   LEFT JOIN {2} ON auth_user_groups.user_id =  auth_user.id
                                   WHERE auth_group.name = 'student'
                                   """.format('auth_user_groups', 'auth_group', 'auth_user'))