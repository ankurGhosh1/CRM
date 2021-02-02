from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentCreate
from .mixins import UnauthRequiredMixin

# Create your views here.
class AgentListView(UnauthRequiredMixin, generic.ListView):
    template_name = 'agents.html'
    
    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)


class AgentCreateView(UnauthRequiredMixin, generic.CreateView):
    template_name = 'agentcreate.html'
    form_class = AgentCreate

    def get_success_url(self):
        return reverse('agents:agents')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.company = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(UnauthRequiredMixin, generic.DetailView):
    template_name = 'agentdetail.html'

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)

class AgentUpdateView(UnauthRequiredMixin, generic.UpdateView):
    template_name = 'agentupdate.html'
    form_class = AgentCreate

    def get_success_url(self):
        return reverse('agents:agents')

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)

class AgentDeleteView(UnauthRequiredMixin, generic.DeleteView):
    template_name = 'agentdelete.html'

    def get_queryset(self):
        company = self.request.user.userprofile
        return Agent.objects.filter(company=company)

    def get_success_url(self):
        # return "/all"
        return reverse("agents:agents")