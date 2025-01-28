from django.db import models


class Calendar(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    # TODO: add isActive field

    def __str__(self):
        return self.name
