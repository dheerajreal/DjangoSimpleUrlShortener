from django.db import models
from .utilities import short_url_generate


class UrlRecord(models.Model):
    original_url = models.URLField(blank=False, null=False)
    short_url = models.CharField(
        primary_key=True, editable=False, max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
