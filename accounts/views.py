from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from accounts.forms import EditForm

User = get_user_model()


class ProfileView(FormView):
    template_name = 'profile.html'
    form_class = EditForm

    def get_success_url(self):
        return reverse('profile', self.request.user.id)
