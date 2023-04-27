import re

EMAIL_ADDRESS_PATTERN = re.compile(
    r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
)
PHONE_NUMBER_PATTERN = re.compile('^[0-9]{10}$')
COLOR_CODE_PATTERN = re.compile('^(?:[0-9a-fA-F]{3}){2}$')


def is_valid_phone(phone: str) -> bool:
    return PHONE_NUMBER_PATTERN.match(phone) is not None if phone else False


def is_valid_email(email: str) -> bool:
    return EMAIL_ADDRESS_PATTERN.match(email) is not None if email else False
