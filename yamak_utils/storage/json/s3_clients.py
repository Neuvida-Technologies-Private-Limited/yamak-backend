import json

from .entities import JSONStorage
from ..others.s3_base import S3Base


class S3JSONStorage(S3Base, JSONStorage):

    def __init__(self, bucket_name: str, region: str, access_key: str, secret_key: str):
        super().__init__(
            bucket_name=bucket_name,
            region=region,
            access_key=access_key,
            secret_key=secret_key,
        )

    def save(self, file_key: str, json_data) -> str:

        # Converting request_id to str instead of UUID
        json_data['request_id'] = str(json_data['request_id'])

        self.s3_client.put_object(
            Body=str(json.dumps(json_data)),
            Bucket=self.bucket,
            Key=file_key,
        )
        return file_key