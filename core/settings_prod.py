from .settings_base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = [
    #your hosting domain
]


# STATICFILES_DIRS =[BASE_DIR/'react/dist', 
# '/var/www/static/',]

#using PyhtonAnywhere's database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('ENGINE')),
        'USER': str(os.getenv('USER')),
        'PASSWORD': str(os.getenv('PASSWORD')),
        'HOST': str(os.getenv('HOST')),
        'PORT': str(os.getenv('PORT')),
        'OPTIONS':{'isolation_level':None}
    }
}

CORS_ALLOWED_ORIGINS = [
    # host from the requesting site
]