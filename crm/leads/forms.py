from django import forms
from .models import Lead, LeadDetail, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

# class LeadForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     age = forms.IntegerField(min_value=0)
#     city = forms.CharField(max_length=25)
#     country = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=50)
#     agent = forms.CharField(max_length=50, required=False)
#     status = forms.CharField(max_length=15)
#     avatar = forms.ImageField()

class LeadForm(forms.ModelForm):
    class Meta: 
        model = Lead
        fields = '__all__'
           

class LeadDetailForm(forms.ModelForm):
    class Meta: 
        model = LeadDetail
        fields = '__all__'

# (
#     'first_name',
#     'last_name',
#     'age',
#     'city',
#     'country',
#     'email',
#     'agent',
#     'status',
#     'avatar',
# )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}