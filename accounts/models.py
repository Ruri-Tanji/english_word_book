from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError('emailを入力してください！')
        if not username:
            raise ValueError('usernameを入力してください！')
        if not password:
            raise ValueError('passwordを入力してください！')

        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(email, username, password, **kwargs)

    def create_superuser(self, email, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(email, username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = ShortUUIDField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
