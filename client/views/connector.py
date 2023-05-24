from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from main.mixins import validations
from main.mixins.exceptions import BadRequestError
from main.mixins.views import APIResponse
# from yamak_utils

class UploadDataS3View(APIView, APIResponse):
    """Upload the data to S3"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        payload: dict = request.data
 
        # get user
        user = request.user
        request_data = request.POST.dict()
        file_name = login_data.get("file_name")
        print('**** request_data ****', request_data)
        print('**** file_name ****'. file_name)

        response = {
            "file_uploaded": True
        }

        return self.get_success_response(json_response=response)

