import os 
from .settings import *
from .settings import BASE_DIR 
import stripe 

#The trusted urls and domains from which requests can come into our applictation 
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGENS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]

DEBUG = False 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR , 'staticfiles')

connection_string = os.environ["AZURE_MYSQL_CONNECTIONSTRING"]
parameters = {pair.split("=")[0]: pair.split("=")[1] for pair in connection_string.split(";")}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'c7_motors',
        'USER' : 'root' ,
        'PASSWORD' : 'SAna2679627',
        'HOST' : '*', 
        'PORT' :'3306'
    }
}


#Payment By STRIPE
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY =os.environ['STRIPE_SECRET_KEY']
STRIPE_WEBHOOK_SECRET = os.environ['STRIPE_WEBHOOK_SECRET']