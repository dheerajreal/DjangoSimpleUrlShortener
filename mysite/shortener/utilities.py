from string import ascii_letters, digits
from random import choices


def short_url_generate():
    all_characters = ascii_letters + digits
    short = choices(all_characters, k=4)
    short = "".join(short)
    return short
