from .settings import (
    HuggingFaceAPISettings
)
from yamak_utils.third_party_models import get_huggingface_client

model_client = get_huggingface_client(
    api_url=HuggingFaceAPISettings.API_URL,
    api_secret=HuggingFaceAPISettings.API_SECRET
)
