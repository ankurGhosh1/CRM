from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_company = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


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
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=15, choices=lead_status, null=True)
    avatar = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return self.first_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.user.username


class LeadDetail(models.Model):
    Lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    files = models.FileField(blank=True, upload_to='media')
    tasks = models.TextField(max_length=1000)

    def __str__(self):
        return self.Lead.first_name


def post_user_created(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created, sender=User)
