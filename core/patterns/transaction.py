from django.utils import timezone

from core.model.test.records import TestRecord


class TestTransactionScript:
    test = None

    @classmethod
    def create_test(self, test_data=None):
        errors = {}

        if not "title" in test_data:
            errors['title'] = {
                "message": "Обязательноe поле"
            }

        if not "description" in test_data:
            errors['description'] = {
                "message": "Обязательноe поле"
            }

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
    def change_test(self, test_data):
        errors = {}

        if not "title" in test_data:
            errors['title'] = {
                "message": "Обязательноe поле"
            }

        if not "description" in test_data:
            errors['description'] = {
                "message": "Обязательноe поле"
            }

        if self.test is None and not errors:
            self.test = TestRecord(user_id=test_data['user'],
                                   title=test_data['title'],
                                   creation_date=timezone.now,
                                   description=test_data['description'],
                                   total_points=100)

            self.test.save()
        else:
            return errors
