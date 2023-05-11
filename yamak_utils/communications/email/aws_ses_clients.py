import boto3

from .entities import EmailClient, EmailDeliveryStatus, \
    EmailDeliveryData, EmailDetail, EmailAttachments
from ...storage.cache.entities import KeyValueCacheStorage

class AWSSESClient(EmailClient):

    def __init__(
        self,
        region: str,
        access_key: str,
        secret_key: str,
        unique_email_cache: KeyValueCacheStorage,
        unique_email_ttl: int,
    ) -> None:
        '''
        unique_email_cache is to hold email for unique_email_ttl time
        so that same email should not go to customer in case of any client bug
        '''
        self.__ses_client = boto3.client(
            "ses",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        self.__cache = unique_email_cache
        self.__unique_email_ttl = unique_email_ttl

    def send(
        self,
        email_detail: EmailDetail,
        attachments: list[EmailAttachments]
    ) -> EmailDeliveryData:
        if self.__cache.contains(key=email_detail.unique_email_id):
            return EmailDeliveryData(
                status=EmailDeliveryStatus.DUPLICATE,
                error=f'email with unique id: {email_detail.unique_email_id} was already sent'
            )

        try:
            # todo: send prepare response data
            self.__cache.add(
                key=email_detail.unique_email_id,
                value=1,
                time_to_live=self.__unique_email_ttl,
            )
            return EmailDeliveryData(
                status=EmailDeliveryStatus.SUCCESS,
            )
        except Exception as exc:
            return EmailDeliveryData(
                status=EmailDeliveryStatus.FAILED,
                error=str(exc)
            )