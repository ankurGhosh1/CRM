from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('leads/', views.leads, name="leads"),
    path('newlead/', views.newlead, name="newlead"),
    path('leads/<int:pk>', views.lead_details, name="lead-details"),
    path('leads/<int:pk>/update', views.lead_update, name="lead-update"),
    path('leads/<int:pk>/delete', views.lead_delete, name="lead-delete"),
]