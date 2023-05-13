import boto3
from access.services import auth_service
from access.services import profile_service
from main import IS_PRODUCTION
from main.mixins.exceptions import BadRequestError
from main.settings import env


def generate_otp(email: str):
    """Generate and send OTP to phone"""

    otp = auth_service.create_otp(email=email)
    if IS_PRODUCTION or not env.OTP_DISABLED:
        return otp

def send_otp(email: str,  otp: str):
    """Send the otp to the email"""

    # Create an SES client
    client = boto3.client(
        "ses",  
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
        region_name=env.REGION_NAME
    )

    response = client.send_email(
        Destination={
            'ToAddresses': [
                str(email)
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': '<p>' + str(otp) + ' is the OTP for logging into Yamak AI' + '</p>',
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': str(otp) + ' is the OTP for logging into Yamak AI',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Yamak AI OTP',
            },
        },
        Source='admin@yamak.ai',
    )

    if response.get('ResponseMetadata').get('HTTPStatusCode') != 200:
        raise BadRequestError('unable to send otp to email')

def verify_otp(email: str, otp: str) -> dict[str, str]:
    """Verify OTP, create an access and refresh token"""

    if IS_PRODUCTION or not env.OTP_DISABLED:
        otp_entry = auth_service.get_otp(email=email, otp=otp)
        if not otp_entry:
            raise BadRequestError('incorrect otp')

    user = profile_service.get_user(email=email)
   
    # update last login
    profile_service.update_last_login(user=user)
    
    # generate tokens
    tokens = auth_service.create_auth_tokens(user=user)
    
    if otp_entry:
        # expire OTP if exists
        auth_service.expire_otp(otp_entry=otp_entry)

    return tokens
