from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_l03unw')

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f'{self.title} by {self.owner}'
