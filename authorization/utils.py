import re
from rest_framework.exceptions import ValidationError
import random


def otp_code_generator():
    return random.randint(10000, 99999)


def pronouns_validator(word):
    pattern = r'^[a-z]{2,5}/[a-z]{2,5}$'
    if not re.match(pattern, word):
        return
    return True


def validate_password(string):
    pattern = (
        r'^(?=.*[a-z])'  # At least one lowercase letter
        r'(?=.*\d)'  # At least one digit
        r'[A-Za-z\d@$!%*?&]{8,}$'  # Allowed characters and at least 8 characters long
    )
    if not re.match(pattern, string):
        return False
    return True
