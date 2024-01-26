from allauth.account.views import logout
from django.urls import reverse_lazy
from django.views import generic

from .models import BaseRegisterForm

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
class LogOutView(generic.RedirectView):
    url = reverse_lazy('')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
