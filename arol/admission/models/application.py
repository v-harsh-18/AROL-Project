from django.db import models
from django.utils.translation import gettext as _
from .advertisement import Advertisement
from .profile import Profile


class Application(models.Model):

    application_id = models.CharField(
        _("Application ID"), unique=True, max_length=13, editable=False
    )
    applicant_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    advertisement_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    payment_id = models.CharField(
        _("Payment ID"), unique=True, max_length=255, blank=True, null=True
    )
    is_approved = models.BooleanField(_("Is Approved"))

    def __str__(self):
        return self.application_id

    def save(self, *args, **kwargs):
        self.application_id = self.advertisement_id + "-" + self.applicant_id

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ["application_id"]