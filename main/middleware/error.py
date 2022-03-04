import logging

from rest_framework import status
from rest_framework.exceptions import ValidationError

from main.mixins import errors
from main.mixins import exceptions
from main.mixins.views import APIResponse

logger = logging.getLogger(__name__)


class APIErrorMiddleware(APIResponse):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # code to be executed before view and later middleware
        response = self.get_response(request)
        # code to be executed after view is called
        return response

    def process_exception(self, request, exception: Exception):
        """
        This will get executed if any exceptions are thrown from a view
        The response of this function will be API response to the client
        Managing different customer error and their response to the client
        """

        _ = request
        # if an invalid or bad request was sent
        # no need to log
        if isinstance(exception, exceptions.BadRequestError):
            return self.get_error_response(
                error_message=exception.message,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        # if an unexpected error happens in the system internally
        # if any unexpected data issues/integrity was found
        # need to log
        # need a user friendly error message
        if isinstance(exception, (exceptions.UnexpectedRequestError, exceptions.DataIssueError)):
            logger.exception(exception)
            return self.get_error_response(
                error_message=errors.UNEXPECTED_ERROR,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # If an unauthorized request comes
        if isinstance(exception, exceptions.UnAuthorizedError):
            logger.exception(exception)
            return self.get_error_response(
                error_message=errors.UNAUTHORIZED_ERROR,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        # Any other validation exception
        # need to log
        # need a user friendly error message
        if isinstance(exception, ValidationError):
            logger.exception(exception)
            return self.get_error_response(
                error_message=exception.args,
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        # Resource not fond
        # need to log if alert_error is True
        # need a user friendly error message
        if isinstance(exception, exceptions.NotFoundError):
            if exception.alert_error:
                logger.exception(exception)
            return self.get_error_response(
                error_message=errors.NOT_FOUND_ERROR,
                status_code=status.HTTP_404_NOT_FOUND,
            )

        # Any other exception
        # need to log
        # need a user friendly error message
        if isinstance(exception, Exception):
            logger.exception(exception)
            return self.get_error_response(
                error_message=errors.UNEXPECTED_ERROR,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
