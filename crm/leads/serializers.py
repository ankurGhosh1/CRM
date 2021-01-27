from rest_framework import serializers
from .models import User, Lead, Agent

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'