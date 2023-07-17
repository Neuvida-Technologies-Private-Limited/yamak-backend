import requests
from .entities import ModelNameEnum, ModelClient


class HuggingfaceClient(ModelClient):

    def __init__(
            self,
            api_url: str,
            api_secret: str
    ) -> None:
        self.api_url = api_url
        self.api_secret = api_secret

    def get_inference(self, model_input: str, model_name: ModelNameEnum) -> str:
        # Adding auth token in request header
        headers = {
            "Authorization": "Bearer " + str(self.api_secret)
        }

        # Creating payload
        payload = {
            "inputs": model_input,
        }

        model_api_url = self.api_url + model_name

        response = requests.post(model_api_url, headers=headers, json=payload)

        return response.json()
