from django.http import JsonResponse
from rest_framework import status


class APIResponse:

    STATUS_CODE = status

    """All the view should use response format from this class"""

    def get_success_response(self, json_response, status_code=status.HTTP_200_OK):
        """Use this response only if the request was processed successfully"""

        return self.__get_success_response(json_response=json_response, status_code=status_code)

    def get_error_response(self, error_message, status_code):
        """Use this for sending an unsuccessful request"""

        return self.__get_error_response(error_message=error_message, status_code=status_code)

    @classmethod
    def __get_success_response(cls, json_response, status_code):

        return JsonResponse(
            data={
                'is_success': True,
                'data': json_response,
                'error': None,
            },
            status=status_code,
        )

    @classmethod
    def __get_error_response(cls, error_message, status_code):

        return JsonResponse(
            data={
                'is_success': False,
                'data': None,
                'error': {
                    'code': status_code,
                    'message': error_message,
                    'data': None,
                },
            },
            status=status_code,
        )
