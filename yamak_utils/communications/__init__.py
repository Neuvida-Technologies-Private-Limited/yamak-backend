'''
factory functions for communication clients
'''

from .email.aws_ses_clients import AWSSESClient
from .email.entities import EmailDeliveryData
from ..storage.cache.entities import KeyValueCacheStorage

def get_aws_ses_client(
    region: str,
    access_key: str,
    secret_key: str,
    unique_email_cache: KeyValueCacheStorage,
    unique_email_ttl: int,
) -> SMSClient:
    return AWSSESClient(
        region=region,
        access_key=access_key,
        secret_key=secret_key,
        unique_email_cache=unique_email_cache,
        unique_email_ttl=unique_email_ttl,
    )