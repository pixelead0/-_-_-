##
# Logs
##

LOG_PATH = os.path.join(BASE_DIR, "logs")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[BS4_EXAMPLE] %(levelname)s %(name)s %(asctime)s %(module)s %(lineno)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "[BS4_EXAMPLE] %(levelname)s %(name)s %(asctime)s %(module)s %(lineno)d %(thread)d %(message)s"
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_PATH + "/server.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "propagate": True,
            "level": "DEBUG",
        },
    },
}
