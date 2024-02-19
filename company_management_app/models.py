from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=128)
    profile_picture = models.ImageField(upload_to='company_profile_pictures/', null=True, blank=True)