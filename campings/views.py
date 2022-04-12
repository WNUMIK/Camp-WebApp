from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import models


class CreateCampingView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Camping
    fields = ('name', 'place', 'slug', 'overview', 'camping_image')
    template_name = 'campings/create_camping.html'
    permission_required = 'campings.add_camping'
    login_url = reverse_lazy('users:login')
    raise_exception = True
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)