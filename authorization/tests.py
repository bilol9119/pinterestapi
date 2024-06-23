import re


def validate_password(string):
    pattern = (
        r'^(?=.*[a-z])'  # At least one lowercase letter
        r'(?=.*\d)'  # At least one digit
        r'[A-Za-z\d@$!%*?&]{8,}$'  # Allowed characters and at least 8 characters long
    )
    if not re.match(pattern, string):
        return "Please enter a valid password"
    return True


# Example usage
password = "1"
result = validate_password(password)
print(result)  # Should print True if the password is valid
