import re
from django.core.exceptions import ValidationError


def pronouns_validator(word):
    pattern = r'^[a-z]{0,5}/[a-z]{0,5}$'
    if not re.match(pattern, word):
        raise ValidationError(message="please enter valid pattern eg: he/him")
    return True


