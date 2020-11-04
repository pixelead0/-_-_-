import logging

from django.utils.deconstruct import deconstructible

logger = logging.getLogger(__name__)


@deconstructible
class UploadFileConfig(object):

    """Configuración para los archivos que se suben al sistema.
    Se genera un nombre de archivo aleatorio dentro de la ruta seleccionada.
    """

    def __init__(self, sub_path, name):
        self.path = sub_path
        self.name = name

    def __call__(self, instance, filename):
        """Para renombrar archivos al subirlos."""
        from uuid import uuid4
        import os
        from datetime import datetime

        now = datetime.now().strftime("%Y%m%d_%H%M%S")

        ext = filename.split(".")[-1].lower()
        # logger.info(instance.__dict__)
        if instance.pk:
            # Nombre del archivo
            filename = (
                f"{self.name}_{str(instance.pk).zfill(5)}_{now}_{uuid4().hex[:8]}.{ext}"
            )
        else:
            # set filename as random string
            filename = f"{self.name}_{now}_{uuid4().hex[:8]}.{ext}"
        # return the whole path to the file
        return os.path.join(self.path, filename)
