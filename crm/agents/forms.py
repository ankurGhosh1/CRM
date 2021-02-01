from django import forms
from leads.models import Agent

class AgentCreate(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )