from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, nickname, password, **extra):
        user = self.model(username=username, nickname=nickname, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra):
        admin = self.model(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True,
            **extra
        )
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_user(self, username, nickname, password):
        return self._create_user(username, nickname, password)
