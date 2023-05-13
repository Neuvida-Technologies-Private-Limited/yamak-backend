import re

EMAIL_ADDRESS_PATTERN = re.compile(
    r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
)
COLOR_CODE_PATTERN = re.compile('^(?:[0-9a-fA-F]{3}){2}$')

# minimum eight characters, at least one letter, one number and one special character:
PASSWORD_PATTERN = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')

def is_valid_email(email: str) -> bool:
    return EMAIL_ADDRESS_PATTERN.match(email) is not None if email else False

def is_valid_password(password: str) -> bool:
    return PASSWORD_PATTERN.match(password) is not None if password else False
