from .base import *

ALLOWED_HOSTS = ['*']

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}
