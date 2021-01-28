from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Lead(models.Model):
    lead_status = (
        ('Potential', 'Potential'),
        ('Prospect', 'Prospect'),
        ('Negotiation', 'Negotiation'),
        ('Converted', 'Converted'),
        ('Failed', 'Failed')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=25, null=True)
    country = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=15, choices=lead_status, null=True)
    avatar = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return self.first_name



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class LeadDetail(models.Model):
    Lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    files = models.FileField(blank=True, upload_to='media')
    tasks = models.TextField(max_length=1000)

    def __str__(self):
        return self.Lead.first_name
