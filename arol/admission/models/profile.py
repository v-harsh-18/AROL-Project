from django.db import models
from django.utils.translation import gettext as _
from choice.models import Caste_Category, Marital_Status, Gender
from users.models import Account


class Profile(models.Model):

    """
    Personal Profile of an Applicant.
    """

    # Choices
    TYPES = [(True, _("Indian Applicant")), (False, _("Foreign Applicant"))]
    PWD = [(True, _("Yes")), (False, _("No"))]

    applicant_id = models.CharField(_("Applicant ID"), unique=True, max_length=255)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    type_of_applicant = models.BooleanField(
        _("Type of Applicant"), choices=TYPES, default=True
    )
    nationality = models.CharField(_("Nationality"), max_length=255, default="India")

    full_name = models.CharField(_("Full Name"), max_length=255)
    father_or_spouse_name = models.CharField(_("Father's/Spouse Name"), max_length=255)
    date_of_birth = models.DateField(_("Date of Birth"))

    marital_status = models.ForeignKey(Marital_Status, on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    caste_category = models.ForeignKey(Caste_Category, on_delete=models.PROTECT)

    contact_number = models.BigIntegerField(_("Contact Number"))
    parent_contact_number = models.BigIntegerField(_("Parent Contact Number"))

    pwd = models.BooleanField(_("Persons with Disabilities (PwD)"))
    disability = models.CharField(_("Type of Disability"), null=True, max_length=255)

    # For Correspondence
    c_address = models.TextField(_("Address"))
    c_city = models.CharField(_("City"), max_length=255)
    c_state = models.CharField(_("State"), max_length=255)
    c_pin = models.IntegerField(_("Pin/Zip"))

    # Permanent Address
    p_address = models.TextField(_("Address"))
    p_city = models.CharField(_("City"), max_length=255)
    p_state = models.CharField(_("State"), max_length=255)
    p_pin = models.IntegerField(_("Pin/Zip"))

    def __str__(self):
        return self.applicant_id

    def save(self, *args, **kwargs):
        if not self.pwd:
            self.disability = None
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Personal Profile")
        verbose_name_plural = _("Personal Profile")
        ordering = ["applicant_id"]
