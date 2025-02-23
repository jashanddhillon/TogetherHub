from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    MEMBERSHIP_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise'),
    ]

    INTEREST_CHOICES = [
        ('Technology', 'Technology'),
        ('Design', 'Design'),
        ('Business', 'Business'),
    ]
    
    # One-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Fields for membership and interest
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.membership} - {self.interest}"
# Create your models here.
