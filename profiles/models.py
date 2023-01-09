from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../default_profile_ohvixx'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile | Last updated: {self.updated_at}"


# deffo use this code in your project! Links user to profile
# ie creates a new profile for any new user created
@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
