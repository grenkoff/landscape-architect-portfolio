import dj_database_url

from .base import *  # noqa: F401, F403

DEBUG = False

SECRET_KEY = env("SECRET_KEY")  # noqa: F405
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")  # noqa: F405

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600),
}

# Cloudinary media storage
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),  # noqa: F405
    "API_KEY": env("CLOUDINARY_API_KEY"),  # noqa: F405
    "API_SECRET": env("CLOUDINARY_API_SECRET"),  # noqa: F405
}
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
