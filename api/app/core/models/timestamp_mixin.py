from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.core.models import ManagerTimestampMixin


class TimestampMixin(models.Model):
    is_active = models.BooleanField(
        verbose_name=_("Activo"),
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Creado"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Modificado"),
        auto_now=True,
    )

    objects = ManagerTimestampMixin()

    class Meta:
        abstract = True
