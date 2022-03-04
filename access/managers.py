from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone, country):

        user = self.model(
            phone=phone.strip(),
            country=country,
        )
        user.save()
        return user
