class BadRequestError(Exception):
    """
    To be used on invalid request data
    message should be user friendly as it will be shown to the users
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class UnexpectedRequestError(Exception):
    """
    To be used when some unexpected error happens
    This error type will send an alert to raven/sentry/logger from middleware handler
    message should be developer friendly to track the issue
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class DataIssueError(Exception):
    """
    To be used when some data is missing which should not be the case
    A prefixed self.message will be shown to the users
    This error type will send an alert to raven/sentry/logger from middleware handler
    message should be developer friendly to track the issue
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class UnAuthorizedError(Exception):
    """To be used when an unauthorized request comes from client"""

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class NotFoundError(Exception):
    """To be used when a resource was not found"""

    def __init__(self, message, alert_error=True):

        super().__init__(message)
        self.message = message
        self.alert_error = alert_error
