import boto3
from botocore.config import Config


class S3Base:

    def __init__(self, bucket_name: str, region: str, access_key: str, secret_key: str):
        self.bucket = bucket_name
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        self.s3_client = session.client(
            's3',
            region,
            config=Config(s3={'addressing_style': 'path'}),
        )

    def delete(self, file_key: str) -> str:
        self.s3_client.Object(self.bucket, file_key).delete()
        return file_key

    def get_short_time_url(self, file_key, expires_in: int, inline=False, content_type=None) -> str:
        params = {
            'Bucket': self.bucket,
            'Key': file_key,
        }

        if inline:
            params['ResponseContentDisposition'] = 'inline'
        else:
            params['ResponseContentDisposition'] = 'attachment'

        if content_type:
            params['ResponseContentType'] = content_type

        return self.s3_client.meta.client.generate_presigned_url(
            'get_object',
            Params=params,
            ExpiresIn=expires_in,
        )