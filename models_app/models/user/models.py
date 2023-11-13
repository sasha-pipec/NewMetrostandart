from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class User(AbstractUser):
    """Overriding the User model with the email field as primary"""

    username = models.CharField(
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        }, verbose_name="Username",
        unique=True,
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = 'models_app'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
