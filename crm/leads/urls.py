from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import LeadList, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = 'leads'

urlpatterns = [

    # JSON Response


    path('leads/', views.leads, name="leads"),
    path('newlead/', views.newlead, name="newlead"),
    path('leads/<int:pk>', views.lead_details, name="lead-details"),
    path('leads/<int:pk>/update', views.lead_update, name="lead-update"),
    path('leads/<int:pk>/delete', views.lead_delete, name="lead-delete"),
    
    # Template views


    ### FUNCTIONAL ROUTES

    # path('all/', views.all, name="all"),
    # path('lead/<int:pk>', views.eachlead, name="eachlead"),
    # path('lead/<int:pk>/update', views.update_lead, name="update_lead"),
    # path('lead/<int:pk>/delete', views.delete_lead, name="delete_lead"),
    # path('create_lead/', views.create_lead, name="create_lead"),

    path('all/', LeadList.as_view(), name="all"),
    path('lead/<int:pk>', LeadDetailView.as_view(), name="eachlead"),
    path('lead/<int:pk>/update', LeadUpdateView.as_view(), name="update_lead"),
    path('lead/<int:pk>/delete', LeadDeleteView.as_view(), name="delete_lead"),
    path('create-lead/', LeadCreateView.as_view(), name="create-lead"),
]