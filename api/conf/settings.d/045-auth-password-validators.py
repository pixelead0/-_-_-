from datetime import timedelta
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

    # {
    #     'NAME': 'utils.password_validation.CustomCommonPasswordValidator',
    # },
    # {
    #     'NAME': 'utils.password_validation.PasswordHasNumbers',
    #     'OPTIONS': {
    #         'min_value': 3,
    #     }
    # },
    # {
    #     'NAME': 'utils.password_validation.PasswordHasUppers',
    #     'OPTIONS': {
    #         'min_value': 3,
    #     }
    # },
    # {
    #     'NAME': 'utils.password_validation.PasswordHasLowers',
    #     'OPTIONS': {
    #         'min_value': 3,
    #     },
    # },
    # {
    #     'NAME': 'utils.password_validation.PasswordHasSpecialChars',
    #     'OPTIONS': {
    #         'min_value': 1,
    #     },
    # },
]

# Custom user model
# AUTH_USER_MODEL = 'people.Person'

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=1000),
}
