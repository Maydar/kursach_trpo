from core.domains.article.models import Article


class ArticleGateway(object):

    def insert(self, cursor):
        cursor.execute('')

    def delete(self, cursor):
        cursor.execute('')

    def get_all(self):
        return Article.objects.raw("")

    def find_by_title(self):
        return Article.objects.raw("")

    def find_by_user(self):
        return Article.objects.raw("")

    def find_by_date(self):
        return Article.objects.raw("")

    def update(self, cursor):
        cursor.execute('')