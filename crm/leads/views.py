import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import LeadSerializer
from .forms import LeadForm, LeadDetailForm, CustomUserCreationForm
from .models import User, Lead, Agent, LeadDetail


# Create your views here.

#######################
#### Json Response ####
#######################


@csrf_exempt
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



###################  
### Class Views ###
###################

### List View

class LeadList(LoginRequiredMixin, generic.ListView):
    template_name = "leads.html"
    
    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Lead.objects.filter(company=user.userprofile)
        else:
            queryset = Lead.objects.filter(company=user.agent.company)
            queryset = queryset.filter(agent__user=user)
        return queryset
    # print(queryset)
    context_object_name = "leads" ### It is used to change name the template will take. If changed HTML variable needs to be changed. Default name "object_list"
  
### Detail View      

class LeadDetailView(LoginRequiredMixin, generic.DetailView, generic.CreateView):
    template_name = "onelead.html"
    form_class = LeadDetailForm

    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_company:
            queryset = Lead.objects.filter(company=user.userprofile)
        else:
            queryset = Lead.objects.filter(company=user.agent.company)
            queryset = queryset.filter(agent__user=user)
        return queryset


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = self.kwargs.get('pk') # returns partucular user
        context['leadinfo'] = LeadDetail.objects.filter(Lead_id=user)
        return context

    def get_success_url(self):
        # return "/all"
        return reverse("leads:all")

### Create View

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "create.html"
    # queryset = Lead.objects.all()
    form_class = LeadForm
    context_object_name = "lead"

    def get_success_url(self):
        # return "/all"
        return reverse("leads:all")


### Update View

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leadupdate.html"
    queryset = Lead.objects.all()
    form_class = LeadForm
    context_object_name = "lead"

    def get_success_url(self):
        # return "/all"
        return reverse("leads:all")


### Delete View

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        # return "/all"
        return reverse("leads:all")


### Signup View

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    # queryset = Lead.objects.all()
    form_class = CustomUserCreationForm
    context_object_name = "lead"

    def get_success_url(self):
        # return "/all"
        return reverse("leads:login")



######################  
### Function Views ###
######################


### List View

def all(request):
    lead_list = Lead.objects.all() # returns Query set 
    return render(request, "leads.html", {'leads': lead_list})

### Detail View

def eachlead(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    leadinfo = LeadDetail.objects.filter(Lead_id=lead).values() # returns JSON
    print(lead.first_name)
    # print(list(leadinfo)) 
    form = LeadDetailForm()
    if request.method == 'POST':
        form = LeadDetailForm(request.POST, request.FILES)
        # print(form.data)
        if form.is_valid():
            lead = lead.first_name
            form.save()
        return redirect('/all')
    return render(request, "onelead.html", {'lead': lead, 'leadinfo': leadinfo, 'form': LeadDetailForm})

### Create View

def create_lead(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES)
        # print(form.data)
        if form.is_valid():
            form.save()
        return redirect('/all')
    return render(request, 'create.html', {'form': LeadForm})


### Update View

def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/all')
    return render(request, "leadupdate.html", {'lead': lead, 'form': LeadForm})

### Delete View

def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/all')
