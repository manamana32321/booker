from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='resources/', blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
