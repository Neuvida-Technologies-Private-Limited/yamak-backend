from io import BytesIO

from .entities import BlobStorage
from ..others.s3_base import S3Base


class S3BlobStorage(S3Base, BlobStorage):

    def __init__(self, bucket_name: str, region: str, access_key: str, secret_key: str):
        super().__init__(
            bucket_name=bucket_name,
            region=region,
            access_key=access_key,
            secret_key=secret_key,
        )

    def save(self, file_key: str, file_buffer: BytesIO) -> str:

        file_key_copy = str(file_key) + '.pdf'
        file_buffer.seek(0)
        obj = self.s3_client.put_object(Body=file_buffer, Bucket=self.bucket, Key=file_key_copy)

        return file_key_copy