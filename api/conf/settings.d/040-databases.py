# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "NAME": os.getenv("DB_NAME"),
        "ENGINE": os.getenv("DB_ENGINE"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("HOST"),
    },
}
