from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView

from . import models
from .models import Camping


class SearchResultsListView(ListView):
    model = Camping
    context_object_name = 'camping_list'
    template_name = 'campings/search_results.html'


class CampingListView(ListView):
    model = Camping
    template_name = 'campings/camping_list.html'


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


class ReserveCampingView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Reservation
    fields = ('camping', 'start_date', 'end_date', 'people_number')
    template_name = 'campings/reserve_camping.html'
    permission_required = 'campings.view_camping'
    login_url = reverse_lazy('users:login')
    raise_exception = True
    success_url = reverse_lazy('home:home')

    # def form_valid(self, form):
    #     form.instance.regular = self.request.user
    #     return super().form_valid(form)

# class CampingReservation(CreateReservation):
#     model =
