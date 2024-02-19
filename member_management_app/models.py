
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from company_management_app.models import Company


class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=32, blank=False, null=False)
    last_name=models.CharField(max_length=32, blank=False, null=False)
    email=models.EmailField(max_length=128)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created=models.DateTimeField(auto_now=True,editable=False)
    last=models.DateTimeField()
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    def __str__(self):
        return self.username

class MemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    member_card_id=models.CharField(max_length=256)
    
    def __str__(self):
        return self.user.username
    
    
class CompanyMemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='members')
    
    def __str__(self):
        return self.user.username