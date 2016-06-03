from io import StringIO
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from core.patterns.print import XLSPrinter as PrinterWeb
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, TemplateView, ListView, DetailView, RedirectView

from core.domains.test.models import Test, TestResult
from core.forms import UserLoginForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user'] = self.request.user

        return context

class AuthView(FormView):
    http_method_names = ['get', 'post']
    form_class = UserLoginForm
    template_name = 'auth/index.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        redirect_url = self.request.GET.get('next')

        if redirect_url:
            return HttpResponseRedirect(redirect_url)

        return super(AuthView, self).form_valid(form)

    def form_invalid(self, form):
        return super(AuthView, self).form_invalid(form)


class LogoutView(RedirectView):
    url = '/'
    http_method_names = ['get', 'post']

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'test/test_list.html'


class TestResultsAllView(LoginRequiredMixin, ListView):
    model = TestResult
    template_name = 'test/test_result_all.html'


class TestResultsView(LoginRequiredMixin, ListView):
    model = TestResult
    template_name = 'test/test_result_list.html'

    def get_queryset(self):
        student = User.objects.get(pk=self.kwargs.get('student_id'))
        return TestResult.objects.filter(user=student).all()


class TestView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'test/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)

        return context


class TestSearchView(FormView):
    pass


class StudentListView(ListView):
    model = User
    template_name = 'student/student_list.html'

    def get_queryset(self):
        return User.objects.filter(groups__name__in=['student']).all()


class StudentSearchView(FormView):
    pass


class TestEditView(TemplateView):
    template_name = 'test/test_edit.html'

    def get_context_data(self, **kwargs):
        context = super(TestEditView, self).get_context_data(**kwargs)
        context['test'] = Test.objects.get(pk=self.kwargs.get('pk'))
        return context

class TestCreateView(TemplateView):
    template_name = 'test/test_create.html'


class QuestionEditView(TemplateView):
    pass


class TeacherView(TemplateView):
    pass


@login_required
def print_xlsx(request):
    output = BytesIO()
    printer = PrinterWeb()
    output = printer.print(output)
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=report.xlsx"

    return response

