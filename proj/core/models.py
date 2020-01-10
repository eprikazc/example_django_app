from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)
