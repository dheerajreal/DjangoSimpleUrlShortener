from django.db import models
from string import ascii_letters
from random import choices


def short_url_generate():
    short = choices(ascii_letters, k=4)
    short = "".join(short)
    return short


class UrlRecord(models.Model):
    original_url = models.URLField( blank=False, null=False)
    short_url = models.CharField(
        primary_key=True, editable=False, max_length=4, default=short_url_generate)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
