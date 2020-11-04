import logging

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from app.core.models import SaveReversionMixin, TimestampMixin

logger = logging.getLogger(__name__)


class Judgment(SaveReversionMixin, TimestampMixin):
    """Judgment info."""

    url = models.URLField(
        verbose_name=_("URL"),
        max_length=250,
    )

    actor = models.TextField(
        verbose_name=_("Actor"),
        null=False,
    )

    resume = models.TextField(
        verbose_name=_("Resumen"),
        null=False,
    )

    defendant = models.CharField(
        verbose_name=_("Demandado"),
        max_length=300,
        null=False,
    )

    court = models.CharField(
        verbose_name=_("Juzgado"),
        max_length=300,
        null=False,
    )

    state = models.CharField(
        verbose_name=_("Estado"),
        max_length=200,
        null=False,
    )

    case_file = models.TextField(
        verbose_name=_("Expediente"),
        max_length=200,
        null=False,
    )

    notifications = models.IntegerField(
        verbose_name=_("Notificaciones"),
        null=False,
    )

    class Meta:
        verbose_name = _("Lista de Items")
        verbose_name_plural = _("Listas de items")
        # ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.resume}"


@receiver(pre_save, sender=Judgment)
def pre_save_extract_judgment_info_from_url(sender, instance, **kwargs):
    """
    Extract judgment info from url
    """
    from app.main.helpers import JudgmentHelper

    judgment_helper = JudgmentHelper()
    data = judgment_helper.extract_info(instance.url)

    instance.url=data["url"]
    instance.actor=data["actor"]
    instance.defendant=data["defendant"]
    instance.court=data["court"]
    instance.state=data["state"]
    instance.case_file=data["case_file"]
    instance.notifications=data["notifications"]
    instance.resume=data["resume"]
