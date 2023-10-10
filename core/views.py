from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from core.models import Tool, Project


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tools = Tool.objects.all()
        context['tools'] = tools
        projects = Project.objects.all()
        context['projects'] = projects
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
