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


class BaseFormSet(object):

    def __init__(self):
        self.errors = dict()

    def _is_valid_set(self, forms, error_key):
        result = True
        empty_keys = list()

        for key, value in forms.iteritems():
            if not value.is_filled():
                empty_keys.append(key)
            elif not value.is_valid():
                result = False and result
                if error_key not in self.errors:
                    self.errors[error_key] = dict()
                self.errors[error_key][key] = value.errors

        for key in empty_keys:
            forms.pop(key)

        return result