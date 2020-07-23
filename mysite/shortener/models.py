from django.conf import settings
from django.db import models


class UrlRecord(models.Model):
    original_url = models.URLField(blank=False, null=False)
    short_url = models.CharField(
        primary_key=True,
        editable=False,
        max_length=settings.URLTAG_LENGTH
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
