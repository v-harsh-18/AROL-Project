from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.core.signing import Signer
from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext as _


class AccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)

        if not (email):
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _("Email"), max_length=255, primary_key=True, db_index=True
    )
    full_name = models.CharField(_("Full Name"), max_length=255, blank=True)

    is_active = models.BooleanField(_("Is Active"), default=True)
    is_admin = models.BooleanField(_("Is Admin"), default=False)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is SuperUser"), default=False)

    date_joined = models.DateTimeField(_("Joined On"), default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = AccountManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["date_joined"]

    def get_full_name(self):
        """
        Return the full_name of the user.
        """
        return self.full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_activation_mail(self):
        subject = "Activate your Email"
        signed_email = Signer().sign(self.email)
        token = PasswordResetTokenGenerator().make_token(self)
        message = """
        Dear User,

        To activate your account visit:
        http://127.0.0.1:8000/api/verify_email/{signed_email}/{token}/
        
        If the link has expired, click the link below to generate a new link
        http://127.0.0.1:8000/api/generate_link/{signed_email}/
        """.format(
            signed_email=signed_email, token=token
        )
        from_email = settings.EMAIL_HOST_USER
        self.email_user(subject, message, from_email)

    def send_reset_password_mail(self):
        subject = "Reset your Password"
        uidb64 = urlsafe_base64_encode(smart_bytes(self.email))
        token = PasswordResetTokenGenerator().make_token(self)
        message = """
        Dear User,

        To reset your password visit:
        http://127.0.0.1:8000/api/reset_password/{uidb64}/{token}/
        
        If you have not initiated this request, you can safely ignore this mail.
        """.format(
            uidb64=uidb64, token=token
        )
        from_email = settings.EMAIL_HOST_USER
        self.email_user(subject, message, from_email)
