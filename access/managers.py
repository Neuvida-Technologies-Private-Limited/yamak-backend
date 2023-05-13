from django.contrib.auth.base_user import BaseUserManager
from access.constants import UserType

class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, user_type = UserType.ADMIN):

        user = self.model(
            email=email.strip(),
            first_name=first_name,
            last_name=last_name,
            user_type=user_type
        )
        user.save()
        return user
