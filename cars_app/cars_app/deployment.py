import os 
from .settings import *
from .settings import BASE_DIR 
import stripe 

#The trusted urls and domains from which requests can come into our applictation 
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = ['c7-rental-cars-btcpdaf3eqg7czab.uaenorth-01.azurewebsites.net']
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
        'NAME': 'c7-rental-cars-database',
        'USER' : 'dybrwudlpi' ,
        'PASSWORD' : 'SAna2679627',
        'HOST' : 'c7-rental-cars-server.mysql.database.azure.com', 
        'PORT' :'3306'
    }
}


#Payment By STRIPE
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY =os.environ['STRIPE_SECRET_KEY']
STRIPE_WEBHOOK_SECRET = os.environ['STRIPE_WEBHOOK_SECRET']