from django.conf.urls import url

from core import views
from core.views import AuthView, ProfileView, TestListView, TestView, LogoutView, TestResultsView, StudentListView, \
    TestResultsAllView, TestEditView, ArticleListView, \
    ArticleDetailView, ArticleCreateView, ArticleEditView, ArticleDeleteView, TestCreatePlainView, AnswerListView, \
    test_search, student_search, create_test, test_search_all

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='main'),
    url(r'^auth/$', AuthView.as_view(), name='auth'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^test/(?P<pk>\d+)$', TestView.as_view(), name='test'),
    url(r'^test/all$', TestListView.as_view(), name='test_list'),


    url(r'^test/search/$', test_search_all, name='test_search_all'),
    url(r'^test/search/result/$', test_search, name='test_search'),
    url(r'^test/edit/(?P<pk>\d+)$', TestEditView.as_view(), name='test_edit'),
    url(r'^test/create/', TestCreatePlainView.as_view(), name='test_create'),

    url(r'^scores/all/$', TestResultsAllView.as_view(), name='scores_all'),
    url(r'^scores/(?P<student_id>\d+)/$', TestResultsView.as_view(), name='scores'),

    url(r'^report/$', views.print_xlsx, name='print_xlsx'),

    url(r'^student/all/$', StudentListView.as_view(), name='students_all'),
    url(r'^student/search/$', student_search, name='student_search'),

    url(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/create/$', ArticleCreateView.as_view(), name='article_create'),
    url(r'^article/edit/(?P<pk>\d+)$', ArticleEditView.as_view(), name='articles_edit'),
    url(r'^article/delete/(?P<pk>\d+)$', ArticleDeleteView.as_view(), name='article_delete'),

    url(r'^article/all/(?P<author_id>\d+)$', ArticleListView.as_view(), name='articles_by_user'),
    url(r'^article/all/$', ArticleListView.as_view(), name='articles_all'),


    url(r'^answer/list/(?P<student_id>\d+)/(?P<test_id>\d+)$', AnswerListView.as_view(), name='answer_list'),
    url(r'^answers/(?P<student_id>\d+)/(?P<test_id>\d+)$', TestResultsView.as_view(), name='answers'),



]