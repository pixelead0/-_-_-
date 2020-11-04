from django.db import models
from django.utils.translation import ugettext_lazy as _

class ManagerTimestampMixin(models.Manager):
    def actives(self):
        return super().get_queryset().filter(is_active=True)

    def inactives(self):
        return super().get_queryset().filter(is_active=False)
