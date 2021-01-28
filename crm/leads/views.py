from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Lead, Agent, LeadDetail
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import LeadSerializer

# Create your views here.

def leads(request):
    lead_list = Lead.objects.all()
    serializer  = LeadSerializer(lead_list, many=True)
    return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def newlead(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        city = request.POST['city']
        country = request.POST['country']
        email = request.POST['email']
        agent = request.POST['agent']
        status = request.POST['status']
        lead = Lead(
            first_name = first_name,
            last_name = last_name,
            age = age,
            city = city,
            country = country,
            email = email,
            status = status,
        )
        lead.save()
    return redirect('/leads')

@csrf_exempt
def lead_details(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    serializer = LeadSerializer(lead)
    return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def lead_update(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        city = request.POST['city']
        country = request.POST['country']
        email = request.POST['email']
        status = request.POST['status']
        lead.first_name = first_name
        lead.last_name = last_name
        lead.age = age
        lead.city = city
        lead.country = country
        lead.email = email
        lead.status = status
        lead.save()
    return redirect('/leads')

@csrf_exempt
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


    ###################
    #### Templates ####
    ###################


    
def all(request):
    lead_list = Lead.objects.all() # returns Query set 
    return render(request, "leads.html", {'leads': lead_list})

def eachlead(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    leadinfo = LeadDetail.objects.filter(Lead_id=lead).values() # returns JSON
    # print(list(leadinfo)) 
    return render(request, "onelead.html", {'lead': lead, 'leadinfo': leadinfo})


def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/all')