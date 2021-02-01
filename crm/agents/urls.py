from django.urls import path
from .views import AgentListView, AgentCreateView

app_name = 'agents'

urlpatterns = [
    path('agents/', AgentListView.as_view(), name='agents'),
    path('agents-create/', AgentCreateView.as_view(), name='agents-create'),
]