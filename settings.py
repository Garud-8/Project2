# gas_utility_project/settings.py

# Add your Django settings here

# For example:
INSTALLED_APPS = [
    ...
    'customers',
    'support',
    ...
]

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
