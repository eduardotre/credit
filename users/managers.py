from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class NewUserManager(BaseUserManager):
    """New manager to use emails, instead of usernames, for authentication"""

    def create_user(self, email, password, **extra_fields):
        """Create user with email"""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """create superuser with email"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **extra_fields)
