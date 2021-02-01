from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentCreate

# Create your views here.
class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents.html'
    
    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agentcreate.html'
    form_class = AgentCreate

    def get_success_url(self):
        return reverse('agents:agents')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.company = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)