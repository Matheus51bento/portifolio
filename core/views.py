from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, DetailView, CreateView
from core.models import Tool, Project, Contact
from core.forms import ContactForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tools = Tool.objects.all()
        context['tools'] = tools
        projects = Project.objects.all()
        context['projects'] = projects
        context['contact'] = ContactForm()
        return context


class ProjectDetail(DetailView):
    model = Project
    template_name = 'core/project_detail.html'


class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_message = "Sua mensagem foi enviada, em breve entrarei em contato!"
    success_url = reverse_lazy("index")

