from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('agents/', AgentListView.as_view(), name='agents'),
    path('agents-create/', AgentCreateView.as_view(), name='agents-create'),
    path('<int:pk>/', AgentDetailView.as_view(), name="agent-detail"),
    path('agent/<int:pk>/update', AgentUpdateView.as_view(), name="agent-update"),
    path('agent/<int:pk>/delete', AgentDeleteView.as_view(), name="agent-delete"),
]