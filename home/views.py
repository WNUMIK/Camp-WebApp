from django import views
from django.shortcuts import render
from django.views.generic import TemplateView

# from courses.models import Camping, Subject


class HomeView(TemplateView):
    template_name = 'home/home.html'

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #
    #     ctx['courses'] = Camping.objects.all()
    #     ctx['subjects'] = Subject.objects.all()
    #
    #     return ctx
