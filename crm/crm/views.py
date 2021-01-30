from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'


# def home(request):
#     return render(request, 'home.html')