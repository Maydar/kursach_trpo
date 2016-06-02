from django.conf.urls import url

from core.views import AuthView, ProfileView, TestListView, TestView, LogoutView, TestResultsView, StudentListView, \
    TestResultsAllView, StudentSearchView, TestSearchView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='main'),
    url(r'^auth/$', AuthView.as_view(), name='auth'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^test/(?P<pk>\d+)$', TestView.as_view(), name='test'),
    url(r'^test/all$', TestListView.as_view(), name='test_list'),
    url(r'^test_search/$', TestSearchView.as_view(), name='test_search'),

    url(r'^scores/all/$', TestResultsAllView.as_view(), name='scores_all'),
    url(r'^scores/(?P<student_id>\d+)/$', TestResultsView.as_view(), name='scores'),

    url(r'^student/all/$', StudentListView.as_view(), name='students_all'),
    url(r'^student_search/$', StudentSearchView.as_view(), name='student_search'),

    url(r'^answers/(?P<student_id>\d+)/(?P<test_id>\d+)$', TestResultsView.as_view(), name='answers'),
]