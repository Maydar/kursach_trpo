from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import FormView


class AjaxFormView(FormView):
    def success(self, form, message=''):
        return JsonResponse({'status': 'OK', 'message': message})

    def error(self, form, message=''):
        return JsonResponse({'status': 'ERROR', 'message': message})

    def form_valid(self, form):
        form.save()
        return self.success(form)

    def form_invalid(self, form):
        message = form.errors
        return self.error(form, message)

class AuthRedirectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('lk:index')

        return super(AuthRedirectMixin, self).dispatch(request, *args, **kwargs)