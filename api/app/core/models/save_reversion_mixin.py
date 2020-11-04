import logging

import reversion
from django.core.exceptions import FieldDoesNotExist
from django.db import transaction

logger = logging.getLogger(__name__)


class SaveReversionMixin:
    """
    Mixin to override save, wrapping with create_revision.
    To better work keep on left on inheritance.
    """

    def save(self, *args, **kwargs):
        class_name = str(self._meta.verbose_name)
        # logger.info(f"class_name:{class_name} {type(class_name)}")
        with transaction.atomic(), reversion.create_revision():
            # logger.info('save: {}'.format(class_name))
            if self.id:
                # logger.info('actualiza: {}'.format(self))
                reversion.set_comment(f"--- ACTUALIZACION DE {class_name.upper()} ----")
            else:
                # logger.info('nuevo: {}'.format(self))
                reversion.set_comment(f"--- CREACIÓN DE {class_name.upper()} ----")

            try:
                self._meta.get_field('user')
                reversion.set_user(self.user)
            except FieldDoesNotExist:
                reversion.set_user(None)
                # logger.info("[{}] Usuario Anonimo.".format(class_name))
            except Exception as e:
                reversion.set_user(None)


            super(SaveReversionMixin, self).save(*args, **kwargs)
