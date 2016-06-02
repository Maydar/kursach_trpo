from core.domains.test.models import Test, TestResult


class TestGateway(object):
    def insert(self):
        return Test.objects.raw("")

    def delete(self):
        return Test.objects.raw("")

    def get_all(self):
        return Test.objects.raw("")

    def find_by_user(self):
        return Test.objects.raw("")

    def find_by_title(self):
        return Test.objects.raw("")

    def update(self, object):
        return Test.objects.raw("")


class TestResultGateway(object):
    def insert(self):
        return TestResult.objects.raw("")

    def delete(self):
        return TestResult.objects.raw("")

    def get_all(self):
        return TestResult.objects.raw("")

    def find_by_test(self):
        return TestResult.objects.raw("")

    def find_by_user(self):
        return TestResult.objects.raw("")

    def update(self, object):
        return TestResult.objects.raw("")