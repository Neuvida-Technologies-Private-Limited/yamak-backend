from django.conf import settings

_hf_settings = getattr(
    settings,
    'HUGGINGFACE_API_SETTINGS'
)


class HuggingFaceAPISettings:

    API_URL = _hf_settings['API_URL']
    API_SECRET = _hf_settings['API_SECRET']
