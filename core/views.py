from io import StringIO
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
from django.views.generic.edit import BaseUpdateView, BaseDeleteView, FormView, CreateView

from core.base import AjaxFormView
from core.domains.article.models import Article
from core.domains.test.forms import EditTestForm
from core.domains.test.gateways import TestGateway
from core.patterns.print import XLSPrinter as PrinterWeb
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


from core.domains.test.models import Test, TestResult
from core.forms import UserLoginForm, ArticleEditForm, ArticleCreateForm


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



class TestSearchView(LoginRequiredMixin, AjaxFormView):
    pass


class StudentListView(ListView):
    model = User
    template_name = 'student/student_list.html'

    def get_queryset(self):
        return User.objects.filter(groups__name__in=['student']).all()


class StudentSearchView(FormView):
    pass


class TestEditView(LoginRequiredMixin, AjaxFormView):
    template_name = 'test/test_edit.html'
    form_class = EditTestForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['test_instance'] = Test.objects.get(pk=self.kwargs.get('pk'))
        return kwargs


class TestCreateView(CreateView):
    model = Test
    fields = ['title', 'description']
    success_url = reverse_lazy('test_create')

    def form_valid(self, form):
        test = TestGateway(creation_date=timezone.now,
                           user_id=form.cleaned_data['user_id'],
                           title=form.cleaned_data['title'],
                           description=form.cleaned_data['description'],
                           total_points=100)
        test.save()
        return HttpResponseRedirect(self.success_url)


class TestCreatePlainView(TemplateView):
    template_name = 'test/test_create.html'



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_details.html'


class ArticleCreateView(LoginRequiredMixin, AjaxFormView):
    form_class = ArticleCreateForm
    template_name = 'article/article_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user
        return kwargs


class ArticleEditView(LoginRequiredMixin, AjaxFormView, BaseUpdateView):
    model = Article
    fields = ['title', 'text']
    template_name = 'article/article_edit.html'


class ArticleDeleteView(LoginRequiredMixin, AjaxFormView, BaseDeleteView):
    success_url = '/'
    model = Article

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user == self.request.user or self.request.user.is_superuser:
            self.object.delete()
            return JsonResponse({'status': 'OK'})
        else:
            raise Http404('Article not exist')

class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'

    def get_queryset(self):
        if self.kwargs.get('author_id'):
            user= User.objects.get(pk=self.kwargs.get('author_id'))
            self.template_name = 'article/article_list_edit.html'
            return Article.objects.filter(user=user).all()
        else:
            return Article.objects.all()


@login_required
def print_xlsx(request):
    output = BytesIO()
    printer = PrinterWeb()
    output = printer.print(output)
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=report.xlsx"

    return response

