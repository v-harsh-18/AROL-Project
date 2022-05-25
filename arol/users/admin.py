from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    model = Account

    ordering = ("date_joined",)
    search_fields = ("email", "full_name")
    list_display = ("email", "full_name", "date_joined")
    list_filter = ("groups",)

    filter_horizontal = ()
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        (None, {"fields": ("email", "full_name", "password")}),
        (
            _("Permissions"),
            {"fields": ("groups", ("is_active", "is_staff", "is_admin"))},
        ),
        (_("Important Dates"), {"fields": ("date_joined", "last_login")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "groups"),
            },
        ),
    )

admin.site.register(Account, AccountAdmin)
