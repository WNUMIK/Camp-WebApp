from django.views.generic import TemplateView

from campings.models import Camping, Type


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['campings'] = Camping.objects.all()
        ctx['type'] = Type.objects.all()

        return ctx
