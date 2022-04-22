from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from . import models
from .models import Camping


class CampingDetailView(DetailView):
    """
        Showing object details from given model using generic DetailView
    """
    model = Camping
    template_name = 'campings/detail_view.html'


class SearchResultsListView(ListView):
    """
        Search query for objects name using generic ListView
    """
    model = Camping
    template_name = 'campings/search_results.html'

    def get_queryset(self):
        """
            Override method for queryset searching for query containing name of given object
             from given model
        """
        q = self.request.GET.get('q')
        if q:
            camping_list = self.model.objects.filter(name__icontains=q)
        else:
            camping_list = self.model.objects.none()
        return camping_list


class CampingListView(ListView):
    """
        List of objects using generic ListView
    """

    model = Camping
    template_name = 'campings/camping_list.html'


class CreateCampingView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
        Adding new object to model by form view using generic django views fn
    """
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
    """
        Reservation view for given model using generic django views fn
    """

    model = models.Reservation
    fields = ('camping', 'check_in', 'check_out', 'people_number')
    template_name = 'campings/reserve_camping.html'
    permission_required = 'campings.add_reservation'
    login_url = reverse_lazy('users:login')
    raise_exception = True
    success_url = reverse_lazy('home:home')

    def get_form(self, form_class=None):
        """
            Override method for form to display date type
        """
        form = super().get_form(form_class)
        form.fields['check_in'].widget = forms.TextInput(
            attrs={'type': 'date'}
        )
        form.fields['check_out'].widget = forms.TextInput(
            attrs={'type': 'date'}
        )
        return form

    def form_valid(self, form):
        form.instance.regular = self.request.user
        return super().form_valid(form)
