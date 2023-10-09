from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Tool


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tools = Tool.objects.all()
        context['tools'] = tools
        return context
