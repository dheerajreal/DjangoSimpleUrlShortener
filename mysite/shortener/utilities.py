from random import choices
from string import ascii_letters, digits

from django.conf import settings


def short_url_generate():
    all_characters = ascii_letters + digits
    short = choices(all_characters, k=settings.URLTAG_LENGTH)
    short = "".join(short)
    return short
