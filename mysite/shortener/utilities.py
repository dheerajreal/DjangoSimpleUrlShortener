from string import ascii_letters, digits
from random import choices

URLTAG_LENGTH = 4


def short_url_generate():
    all_characters = ascii_letters + digits
    short = choices(all_characters, k=URLTAG_LENGTH)
    short = "".join(short)
    return short
