'''
factory functions for storage
'''

from .blob.entities import BlobStorage
from .blob.s3_clients import S3BlobStorage
from .cache.entities import KeyValueCacheStorage
from .cache.redis_clients import RedisKeyValueCacheStorage
from .json.entities import JSONStorage
from .json.s3_clients import S3JSONStorage
from ..loggers.tri_request_logger import TPIRequestLogger

def get_redis_key_value_cache_storage(host: str, port: str) -> KeyValueCacheStorage:
    return RedisKeyValueCacheStorage(host, port)


def get_aws_s3_blob_storage(
    bucket_name: str,
    region: str,
    access_key: str,
    secret_key: str,
) -> BlobStorage:
    return S3BlobStorage(
        bucket_name=bucket_name,
        region=region,
        access_key=access_key,
        secret_key=secret_key,
    )

def get_tri_request_logger(
    bucket_name,
    region,
    access_key,
    secret_key
) -> JSONStorage:
    return TPIRequestLogger(
        json_storage=get_aws_s3_json_storage(
            bucket_name,
            region,
            access_key,
            secret_key
        ),
    )

def get_aws_s3_json_storage(
    bucket_name: str,
    region: str,
    access_key: str,
    secret_key: str,
) -> JSONStorage:
    return S3JSONStorage(
        bucket_name=bucket_name,
        region=region,
        access_key=access_key,
        secret_key=secret_key,
    )