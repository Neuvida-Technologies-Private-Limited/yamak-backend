'''
factory functions for model features
'''

from .huggingface_client import HuggingfaceClient


def get_huggingface_client(
    api_url: str,
    api_secret: str
) -> HuggingfaceClient:
    return HuggingfaceClient(
        api_url = api_url,
        api_secret = api_secret
    )