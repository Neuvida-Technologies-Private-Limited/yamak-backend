from rest_framework.views import APIView
from main.mixins.exceptions import BadRequestError
from main.mixins.views import APIResponse
from ai_models.tpi import model_client
from yamak_utils.third_party_models.entities import ModelNameEnum


class GetModelInferenceView(APIView, APIResponse):
    """Update the password of the user"""

    def post(self, request):

        payload: dict = request.data

        # Extracting the input param from the request
        input = payload.get('input', None)

        if not input:
            raise BadRequestError('invalid input')

        model_name = payload.get('model_name', None)

        if not model_name:
            raise BadRequestError('invalid model name')

        output = model_client.get_inference(input, model_name)

        response = {
           "output": output
        }

        return self.get_success_response(json_response=response)


class GetModelListView(APIView, APIResponse):
    """Update the password of the user"""

    def get(self, request):

        # Converting the mode
        constant_list = [e.value for e in ModelNameEnum]
        print('vars(ModelNameEnum).values()', [e.value for e in ModelNameEnum])
        response = {
           "output": constant_list
        }

        return self.get_success_response(json_response=response)
