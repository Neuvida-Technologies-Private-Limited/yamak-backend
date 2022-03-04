from rest_framework.serializers import ModelSerializer

from access.models import User
from main.mixins import errors
from main.mixins.exceptions import BadRequestError
from main.mixins.validations import is_valid_phone


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['phone', 'country']

    @staticmethod
    def validate_phone(phone):

        if not is_valid_phone(phone=phone):
            raise BadRequestError('invalid phone number')

        return phone

    def update(self, instance, validated_data):
        errors.raise_serializer_not_implemented_error(type(self), 'update')

    @property
    def data(self):
        errors.raise_serializer_not_implemented_error(type(self), 'data')
