from string import ascii_letters, digits
from random import choices

# 4 characters=62**4=14,776,336 combinations
# 5 characters=62**5=916,132,832 combinations
# 6 characters=62**6=56,800,235,584 combinations
# pick one of these
URLTAG_LENGTH = 4


def short_url_generate():
    all_characters = ascii_letters + digits
    short = choices(all_characters, k=URLTAG_LENGTH)
    short = "".join(short)
    return short
