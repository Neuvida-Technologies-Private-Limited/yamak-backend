"""Maintain all generic errors"""
from .exceptions import UnexpectedRequestError

UNEXPECTED_ERROR = 'unexpected error'
UNAUTHORIZED_ERROR = 'not authorized'
NOT_FOUND_ERROR = 'resource not found'


def raise_serializer_not_implemented_error(serializer_type: type, method: str):
    """raise unexpected error if a serializer method is not implemented"""

    # the error will be considered as unexpected
    # developer should not implement these restricted methods
    error = f'{serializer_type.__name__} {method} is not implemented'
    raise UnexpectedRequestError(error)
