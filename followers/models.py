from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Follower(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"{self.followed} followed by {self.owner}"


# raises the same Integrity error from serializer if user tries
# to follow themselves
@receiver(pre_save, sender=Follower)
def stop_self_follow(sender, instance, **kwargs):
    if instance.owner == instance.followed:
        raise IntegrityError()
