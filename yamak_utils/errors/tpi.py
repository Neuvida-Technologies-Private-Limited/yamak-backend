'''
TPI: third party integration related
'''


class PreTPIValidationError(Exception):
    """
    To be used for invalid input data before sending to third party api
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class PostTPIError(Exception):
    """
    To be used when a third party call fails
    """

    def __init__(self, message, error_content):

        super().__init__(message)
        self.message = message
        self.error_content = error_content


class DataSignatureFailedError(Exception):
    """
    To be used when verifying signature from TP webhooks and others
    """

    def __init__(self, message):

        super().__init__(message)
        self.message = message


class TPIRequestLoggerFailedError(Exception):
    """
    To be used when verifying signature from TP webhooks and others
    """

    def __init__(self, message, request_data):

        super().__init__(message)
        self.message = message
        self.request_data = request_data