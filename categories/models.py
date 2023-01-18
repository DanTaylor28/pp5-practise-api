from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # use timestamp instead
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
