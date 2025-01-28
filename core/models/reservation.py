from django.db import models
from .resource import Resource


class Reservation(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    # TODO: add user field
    description = models.TextField(blank=True)

    startDatetime = models.DateTimeField()
    endDatetime = models.DateTimeField()
    
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
    # TODO: add isPublic field

    def __str__(self):
        return f'{self.resource} - {self.user}'